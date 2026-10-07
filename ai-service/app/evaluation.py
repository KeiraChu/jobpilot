from app.schemas import EvaluationCase, EvaluationResult


def evaluate(case: EvaluationCase) -> EvaluationResult:
    ranked = case.ranked_position_ids[: case.k]
    relevant = set(case.relevant_position_ids)
    hits = [position_id for position_id in ranked if position_id in relevant]
    recall = len(hits) / len(relevant) if relevant else 0.0
    precision = len(hits) / len(ranked) if ranked else 0.0
    rr = next((1 / (i + 1) for i, value in enumerate(ranked) if value in relevant), 0.0)
    return EvaluationResult(recall_at_k=recall, precision_at_k=precision, reciprocal_rank=rr)

