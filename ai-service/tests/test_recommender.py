import asyncio

from app.parsing import heuristic_profile
from app.recommender import recommend_positions
from app.schemas import PositionInput, RecommendRequest


class FakeProvider:
    async def embed(self, texts):
        vectors = []
        for text in texts:
            lowered = text.lower()
            vectors.append([
                1.0 if "python" in lowered or "ai" in lowered else 0.0,
                1.0 if "会计" in text or "财务" in text else 0.0,
            ])
        return vectors

    async def json(self, messages, schema, name):
        return {"judgments": [
            {
                "position_id": 1,
                "relevance_score": 96,
                "summary": "岗位要求与简历中的 Python、FastAPI 证据一致",
                "evidence_skills": ["python", "fastapi", "不存在的技能"],
                "missing_skills": [],
            },
            {
                "position_id": 2,
                "relevance_score": 10,
                "summary": "岗位方向与目标不一致",
                "evidence_skills": [],
                "missing_skills": [],
            },
        ]}


class IncompleteProvider(FakeProvider):
    async def json(self, messages, schema, name):
        return {"judgments": [{
            "position_id": 1, "relevance_score": 90, "summary": "不完整结果",
            "evidence_skills": ["python"], "missing_skills": [],
        }]}


def test_embedding_and_llm_rerank_preserve_evidence_boundary():
    profile = heuristic_profile("Python FastAPI RAG 项目经验", "AI应用开发")
    request = RecommendRequest(user_id="1", profile=profile, positions=[
        PositionInput(position_id=1, company="A", title="AI应用开发", description="Python FastAPI RAG"),
        PositionInput(position_id=2, company="B", title="会计", description="财务报表"),
    ], top_k=2)

    outcome = asyncio.run(recommend_positions(request, FakeProvider(), rerank_candidates=2))

    assert outcome.ranking_mode == "LLM_RERANK"
    assert outcome.results[0].position.position_id == 1
    assert "简历技能：python" in outcome.results[0].evidence
    assert all("不存在的技能" not in item for item in outcome.results[0].evidence)


def test_recommender_falls_back_without_model_provider():
    profile = heuristic_profile("Python FastAPI RAG 项目经验", "AI应用开发")
    request = RecommendRequest(user_id="1", profile=profile, positions=[
        PositionInput(position_id=1, company="A", title="AI应用开发", description="Python FastAPI RAG"),
    ])

    outcome = asyncio.run(recommend_positions(request, None))

    assert outcome.ranking_mode == "BASELINE"
    assert outcome.results[0].position.position_id == 1


def test_incomplete_llm_result_falls_back_to_embedding():
    profile = heuristic_profile("Python FastAPI RAG 项目经验", "AI应用开发")
    request = RecommendRequest(user_id="1", profile=profile, positions=[
        PositionInput(position_id=1, company="A", title="AI应用开发", description="Python FastAPI RAG"),
        PositionInput(position_id=2, company="B", title="会计", description="财务报表"),
    ], top_k=2)

    outcome = asyncio.run(recommend_positions(request, IncompleteProvider(), rerank_candidates=2))

    assert outcome.ranking_mode == "EMBEDDING"
    assert any("模型重排不可用" in warning for warning in outcome.warnings)
