import argparse
import asyncio
import json
import time
from datetime import datetime, timezone
from pathlib import Path

from app.config import Settings
from app.evaluation import evaluate
from app.parsing import structured_profile
from app.provider import ModelProvider
from app.recommender import recommend_positions
from app.schemas import EvaluationCase, RecommendRequest
from evals.benchmark import POSITIONS, benchmark_profiles


async def run(limit: int | None) -> dict:
    settings = Settings()
    if not settings.api_key:
        raise SystemExit("AI_API_KEY is required; no report was overwritten")
    provider = ModelProvider(settings)
    cases = benchmark_profiles()[:limit] if limit else benchmark_profiles()
    results, latencies, modes = [], [], {}
    provider.reset_usage()
    try:
        for case in cases:
            started = time.perf_counter()
            profile = await structured_profile(case["resume_text"], case["target_role"], provider)
            outcome = await recommend_positions(
                RecommendRequest(user_id=case["case_id"], profile=profile, positions=POSITIONS, top_k=5),
                provider,
            )
            latencies.append((time.perf_counter() - started) * 1000)
            modes[outcome.ranking_mode] = modes.get(outcome.ranking_mode, 0) + 1
            results.append(evaluate(EvaluationCase(
                relevant_position_ids=case["relevant_position_ids"],
                ranked_position_ids=[item.position.position_id for item in outcome.results],
                k=5,
            )))
    finally:
        usage = provider.usage_summary()
        await provider.close()
    ordered_latency = sorted(latencies)
    return {
        "dataset": "synthetic-redacted-v2",
        "model": settings.chat_model,
        "embedding_model": settings.embedding_model,
        "cases": len(results),
        "ranking_modes": modes,
        "recall_at_5": round(sum(item.recall_at_k for item in results) / len(results), 4),
        "precision_at_5": round(sum(item.precision_at_k for item in results) / len(results), 4),
        "mrr": round(sum(item.reciprocal_rank for item in results) / len(results), 4),
        "mean_latency_ms": round(sum(latencies) / len(latencies), 2),
        "p95_latency_ms": round(ordered_latency[max(0, int(len(ordered_latency) * 0.95) - 1)], 2),
        "model_usage": usage,
    }


async def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None, help="Run a smaller paid smoke test before the full 60-case evaluation")
    args = parser.parse_args()
    result = await run(args.limit)
    report_path = Path(__file__).parents[2] / "docs/real-model-evaluation.md"
    report = "# 真实模型评测报告\n\n" + f"- 执行时间：{datetime.now(timezone.utc).isoformat()}\n- 状态：已执行\n\n```json\n{json.dumps(result, ensure_ascii=False, indent=2)}\n```\n"
    report_path.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    asyncio.run(main())
