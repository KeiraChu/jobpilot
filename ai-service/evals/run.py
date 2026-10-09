import json

from app.evaluation import evaluate
from app.parsing import heuristic_profile
from app.ranking import rank
from app.schemas import EvaluationCase, RecommendRequest
from evals.benchmark import POSITIONS, benchmark_profiles


results = []
for case in benchmark_profiles():
    profile = heuristic_profile(case["resume_text"], case["target_role"])
    ranked = rank(RecommendRequest(user_id=case["case_id"], profile=profile, positions=POSITIONS, top_k=5))
    results.append(evaluate(EvaluationCase(
        relevant_position_ids=case["relevant_position_ids"],
        ranked_position_ids=[item.position.position_id for item in ranked],
        k=5,
    )))

summary = {
    "dataset": "synthetic-redacted-v2",
    "ranking_mode": "BASELINE",
    "cases": len(results),
    "recall_at_5": round(sum(x.recall_at_k for x in results) / len(results), 4),
    "precision_at_5": round(sum(x.precision_at_k for x in results) / len(results), 4),
    "mrr": round(sum(x.reciprocal_rank for x in results) / len(results), 4),
}
print(json.dumps(summary, ensure_ascii=False, indent=2))
