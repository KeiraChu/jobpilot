from app.evaluation import evaluate
from app.parsing import heuristic_profile
from app.ranking import rank
from app.schemas import EvaluationCase, PositionInput, RecommendRequest


def test_ai_position_ranks_first():
    profile = heuristic_profile("Python FastAPI RAG pgvector 项目经验", "AI应用开发")
    positions = [
        PositionInput(position_id=1, company="A", title="AI应用开发", description="Python FastAPI RAG pgvector"),
        PositionInput(position_id=2, company="B", title="会计", description="财务报表与税务"),
    ]
    result = rank(RecommendRequest(user_id="1", profile=profile, positions=positions, top_k=2))
    assert result[0].position.position_id == 1
    assert "python" in result[0].matched_skills


def test_metrics():
    result = evaluate(EvaluationCase(relevant_position_ids=[2, 3], ranked_position_ids=[1, 2, 4], k=3))
    assert result.recall_at_k == 0.5
    assert result.reciprocal_rank == 0.5


def test_chinese_role_similarity_and_city_constraint_affect_ranking():
    profile = heuristic_profile("大模型应用开发，使用 Python 与 RAG", "AI应用开发")
    profile.city_preferences = ["上海"]
    positions = [
        PositionInput(position_id=1, company="A", title="人工智能应用开发实习生", description="Python RAG", address="上海"),
        PositionInput(position_id=2, company="B", title="人工智能应用开发实习生", description="Python RAG", address="北京"),
    ]
    result = rank(RecommendRequest(user_id="1", profile=profile, positions=positions, top_k=2))
    assert result[0].position.position_id == 1
    assert result[0].breakdown.preference > 0
    assert result[0].score > result[1].score
