import json
from pathlib import Path

from app.evaluation import evaluate
from app.schemas import EvaluationCase

cases = [EvaluationCase(**json.loads(line)) for line in Path(__file__).with_name("cases.jsonl").read_text().splitlines()]
results = [evaluate(case) for case in cases]
print(json.dumps({
    "cases": len(results),
    "recall_at_k": sum(x.recall_at_k for x in results) / len(results),
    "precision_at_k": sum(x.precision_at_k for x in results) / len(results),
    "mrr": sum(x.reciprocal_rank for x in results) / len(results),
}, ensure_ascii=False, indent=2))
