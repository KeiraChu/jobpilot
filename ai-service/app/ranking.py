import math
import re
from collections import Counter

from app.parsing import extract_skills
from app.schemas import MatchResult, PositionInput, RecommendRequest, ScoreBreakdown, SkillGapAction


WEIGHTS = {"semantic": 0.38, "skill_coverage": 0.37, "preference": 0.15, "hard_constraints": 0.10}


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


def improvement_actions(missing: list[str], job_skill_count: int) -> list[SkillGapAction]:
    """Estimate the auditable score gain of adding one verified skill at a time."""
    if not job_skill_count:
        return []
    gain = round(100 * WEIGHTS["skill_coverage"] / job_skill_count, 2)
    return [
        SkillGapAction(
            skill=skill,
            estimated_score_gain=gain,
            evidence_requirement=f"补充能证明 {skill} 的项目任务、代码或结果，经本人确认后再写入简历",
        )
        for skill in missing[:5]
    ]


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
        score = 100 * (
            WEIGHTS["semantic"] * semantic
            + WEIGHTS["skill_coverage"] * coverage
            + WEIGHTS["preference"] * preference
            + WEIGHTS["hard_constraints"] * hard
        )
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
            improvement_actions=improvement_actions(missing, len(job_skills)),
            decision_trace=[
                "只使用岗位文本、简历中的技能证据、目标方向和城市偏好参与排序",
                "不读取性别、年龄、照片等个人属性",
                "补强收益仅估算单项技能覆盖分的变化，不代表录用概率",
            ],
        ))
    return sorted(results, key=lambda x: x.score, reverse=True)[: request.top_k]
