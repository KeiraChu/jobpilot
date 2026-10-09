import json
import math
from dataclasses import dataclass

from app.provider import ModelProvider
from app.ranking import rank
from app.schemas import MatchResult, RecommendRequest


@dataclass
class RecommendationOutcome:
    results: list[MatchResult]
    ranking_mode: str
    algorithm_version: str
    warnings: list[str]


def _profile_text(request: RecommendRequest) -> str:
    profile = request.profile
    descriptions = [
        item.description
        for item in profile.projects + profile.work_experience + profile.education
        if item.description
    ]
    return " ".join([profile.target_role, profile.summary, " ".join(profile.skills), *descriptions])[:8000]


def _position_text(result: MatchResult) -> str:
    position = result.position
    return " ".join([position.title, position.description, position.education, position.address])[:4000]


def _cosine(left: list[float], right: list[float]) -> float:
    numerator = sum(a * b for a, b in zip(left, right))
    denominator = math.sqrt(sum(a * a for a in left)) * math.sqrt(sum(b * b for b in right))
    return numerator / denominator if denominator else 0.0


def _rerank_schema() -> dict:
    judgment = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "position_id": {"type": "integer"},
            "relevance_score": {"type": "number", "minimum": 0, "maximum": 100},
            "summary": {"type": "string"},
            "evidence_skills": {"type": "array", "items": {"type": "string"}},
            "missing_skills": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["position_id", "relevance_score", "summary", "evidence_skills", "missing_skills"],
    }
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {"judgments": {"type": "array", "items": judgment}},
        "required": ["judgments"],
    }


async def recommend_positions(
    request: RecommendRequest,
    provider: ModelProvider | None,
    rerank_candidates: int = 8,
) -> RecommendationOutcome:
    candidate_count = min(max(request.top_k, rerank_candidates), len(request.positions), 20)
    baseline_request = request.model_copy(update={"top_k": candidate_count})
    candidates = rank(baseline_request)
    warnings: list[str] = []
    if provider is None:
        return RecommendationOutcome(
            results=candidates[: request.top_k], ranking_mode="BASELINE",
            algorithm_version="evidence-ranker-v3", warnings=["未配置模型服务，当前使用可解释基线排序。"],
        )

    try:
        embeddings = await provider.embed([_profile_text(request), *[_position_text(item) for item in candidates]])
        resume_embedding, position_embeddings = embeddings[0], embeddings[1:]
        for result, embedding in zip(candidates, position_embeddings):
            semantic = max(0.0, min(1.0, _cosine(resume_embedding, embedding)))
            result.breakdown.semantic = round(semantic * 100, 2)
            result.score = round(0.55 * result.score + 0.45 * semantic * 100, 2)
            result.decision_trace.insert(0, "使用 Embedding 语义相关度与技能证据完成混合召回")
        candidates.sort(key=lambda item: item.score, reverse=True)
    except Exception:
        return RecommendationOutcome(
            results=candidates[: request.top_k], ranking_mode="BASELINE",
            algorithm_version="evidence-ranker-v3", warnings=["Embedding 服务不可用，已降级为可解释基线排序。"],
        )

    shortlist = candidates[: min(rerank_candidates, len(candidates))]
    prompt_positions = [{
        "position_id": item.position.position_id,
        "title": item.position.title,
        "description": item.position.description[:1600],
        "matched_skills": item.matched_skills,
        "missing_skills": item.missing_skills,
        "hybrid_score": item.score,
    } for item in shortlist]
    messages = [
        {"role": "system", "content": (
            "你是求职匹配重排器。只根据输入的简历事实和岗位要求判断，不得推断未提供的经历。"
            "evidence_skills 只能从 matched_skills 选择，missing_skills 只能从同名字段选择。"
            "分数表示材料相关度，不表示录用概率。"
        )},
        {"role": "user", "content": json.dumps({
            "profile": {
                "target_role": request.profile.target_role,
                "skills": request.profile.skills,
                "summary": request.profile.summary[:1800],
            },
            "positions": prompt_positions,
        }, ensure_ascii=False)},
    ]
    try:
        payload = await provider.json(messages, _rerank_schema(), "job_match_rerank")
        by_id = {item.position.position_id: item for item in shortlist}
        for judgment in payload.get("judgments", []):
            result = by_id.get(judgment.get("position_id"))
            if result is None:
                continue
            llm_score = max(0.0, min(100.0, float(judgment.get("relevance_score", 0))))
            result.score = round(0.7 * result.score + 0.3 * llm_score, 2)
            summary = str(judgment.get("summary", "")).strip()
            if summary:
                result.reasons.insert(0, f"模型重排：{summary}")
            allowed_evidence = {skill.lower(): skill for skill in result.matched_skills}
            selected = [allowed_evidence[x.lower()] for x in judgment.get("evidence_skills", []) if x.lower() in allowed_evidence]
            result.evidence = [f"简历技能：{skill}" for skill in selected] or result.evidence
            result.decision_trace.insert(0, "大模型仅在候选集内重排，并受结构化输出与证据白名单约束")
        candidates.sort(key=lambda item: item.score, reverse=True)
        return RecommendationOutcome(
            results=candidates[: request.top_k], ranking_mode="LLM_RERANK",
            algorithm_version="hybrid-embedding-llm-rerank-v1", warnings=warnings,
        )
    except Exception:
        warnings.append("模型重排不可用，已保留 Embedding 混合召回结果。")
        return RecommendationOutcome(
            results=candidates[: request.top_k], ranking_mode="EMBEDDING",
            algorithm_version="hybrid-embedding-v1", warnings=warnings,
        )
