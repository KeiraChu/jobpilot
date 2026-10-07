import math
import re
from collections import Counter

from app.parsing import extract_skills
from app.schemas import MatchResult, PositionInput, RecommendRequest, ScoreBreakdown


def tokens(text: str) -> list[str]:
    lowered = text.lower()
    latin = re.findall(r"[a-zA-Z][a-zA-Z0-9+#.\-]{1,}", lowered)
    chinese_tokens: list[str] = []
    for sequence in re.findall(r"[\u4e00-\u9fff]+", lowered):
        if len(sequence) == 1:
            chinese_tokens.append(sequence)
        else:
            chinese_tokens.extend(sequence[index:index + 2] for index in range(len(sequence) - 1))
    return latin + chinese_tokens


def cosine_text(a: str, b: str) -> float:
    ca, cb = Counter(tokens(a)), Counter(tokens(b))
    if not ca or not cb:
        return 0.0
    common = set(ca) & set(cb)
    numerator = sum(ca[t] * cb[t] for t in common)
    denominator = math.sqrt(sum(v * v for v in ca.values())) * math.sqrt(sum(v * v for v in cb.values()))
    return numerator / denominator if denominator else 0.0


def rank(request: RecommendRequest) -> list[MatchResult]:
    profile = request.profile
    resume_text = " ".join([
        profile.target_role, profile.summary, " ".join(profile.skills),
        *[x.description for x in profile.projects + profile.work_experience + profile.education],
    ])
    resume_skills = {x.lower() for x in profile.skills}
    results = []
    for position in request.positions:
        job_text = f"{position.title} {position.description} {position.education} {position.address}"
        job_skills = {x.lower() for x in extract_skills(job_text)}
        matched = sorted(resume_skills & job_skills)
        missing = sorted(job_skills - resume_skills)
        semantic = cosine_text(resume_text, job_text)
        coverage = len(matched) / len(job_skills) if job_skills else min(semantic * 1.5, 1)
        preference = cosine_text(profile.target_role, position.title) if profile.target_role else 0.5
        city = 1.0 if not profile.city_preferences or any(c in position.address for c in profile.city_preferences) else 0.4
        hard = city
        score = 100 * (0.38 * semantic + 0.37 * coverage + 0.15 * preference + 0.10 * hard)
        evidence = [f"简历技能：{skill}" for skill in matched[:5]]
        reasons = ([f"已覆盖 {len(matched)}/{len(job_skills)} 项可识别技能要求"] if job_skills else ["岗位技能要求较少，主要按语义相关度排序"])
        if preference >= 0.5:
            reasons.append("岗位名称与求职方向相关")
        risks = ([f"缺少明确证据：{skill}" for skill in missing[:5]] or ["未发现明显技能缺口"])
        results.append(MatchResult(
            position=position,
            score=round(score, 2),
            breakdown=ScoreBreakdown(
                semantic=round(semantic * 100, 2), skill_coverage=round(coverage * 100, 2),
                preference=round(preference * 100, 2), hard_constraints=round(hard * 100, 2),
            ),
            matched_skills=matched, missing_skills=missing, evidence=evidence,
            reasons=reasons, risks=risks,
        ))
    return sorted(results, key=lambda x: x.score, reverse=True)[: request.top_k]
