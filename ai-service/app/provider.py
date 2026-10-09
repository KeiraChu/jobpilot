import asyncio
import json
import time
from contextvars import ContextVar

import httpx

from app.config import Settings

_usage: ContextVar[list[dict]] = ContextVar("jobpilot_model_usage", default=[])


class ModelProvider:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.client = httpx.AsyncClient(
            base_url=settings.model_base_url.rstrip("/"), timeout=settings.timeout_seconds,
            headers={"Authorization": f"Bearer {settings.api_key}"},
        )

    async def json(self, messages: list[dict], schema: dict, name: str) -> dict:
        error = None
        for attempt in range(self.settings.max_retries + 1):
            try:
                response = await self.client.post("/chat/completions", json={
                    "model": self.settings.chat_model, "messages": messages, "temperature": 0.1,
                    "response_format": {"type": "json_schema", "json_schema": {"name": name, "strict": True, "schema": schema}},
                })
                response.raise_for_status()
                body = response.json()
                self._record("chat", body.get("usage", {}), self.settings.chat_model)
                return json.loads(body["choices"][0]["message"]["content"])
            except (httpx.HTTPError, KeyError, json.JSONDecodeError) as exc:
                error = exc
                if attempt < self.settings.max_retries:
                    await asyncio.sleep(0.5 * 2**attempt)
        raise RuntimeError("模型服务暂时不可用") from error

    async def embed(self, texts: list[str]) -> list[list[float]]:
        error = None
        for attempt in range(self.settings.max_retries + 1):
            try:
                response = await self.client.post("/embeddings", json={
                    "model": self.settings.embedding_model,
                    "input": texts,
                })
                response.raise_for_status()
                rows = sorted(response.json()["data"], key=lambda item: item["index"])
                if len(rows) != len(texts):
                    raise ValueError("Embedding 返回数量与输入不一致")
                self._record("embedding", response.json().get("usage", {}), self.settings.embedding_model)
                return [row["embedding"] for row in rows]
            except (httpx.HTTPError, KeyError, ValueError) as exc:
                error = exc
                if attempt < self.settings.max_retries:
                    await asyncio.sleep(0.5 * 2**attempt)
        raise RuntimeError("Embedding 服务暂时不可用") from error

    async def close(self):
        await self.client.aclose()

    def reset_usage(self) -> None:
        _usage.set([])

    def usage_summary(self) -> dict:
        calls = _usage.get()
        input_tokens = sum(int(call.get("input_tokens", 0)) for call in calls)
        output_tokens = sum(int(call.get("output_tokens", 0)) for call in calls)
        embedding_tokens = sum(int(call.get("embedding_tokens", 0)) for call in calls)
        estimated_cost = (
            input_tokens * self.settings.chat_input_cost_per_million
            + output_tokens * self.settings.chat_output_cost_per_million
            + embedding_tokens * self.settings.embedding_cost_per_million
        ) / 1_000_000
        return {"model_calls": len(calls), "input_tokens": input_tokens, "output_tokens": output_tokens, "embedding_tokens": embedding_tokens, "estimated_cost": round(estimated_cost, 6), "currency": "CNY"}

    @staticmethod
    def _record(kind: str, usage: dict, model: str) -> None:
        prompt = usage.get("prompt_tokens", usage.get("input_tokens", 0))
        output = usage.get("completion_tokens", usage.get("output_tokens", 0))
        call = {"kind": kind, "model": model, "input_tokens": prompt if kind == "chat" else 0, "output_tokens": output if kind == "chat" else 0, "embedding_tokens": usage.get("total_tokens", prompt) if kind == "embedding" else 0, "recorded_at": time.time()}
        _usage.set([*_usage.get(), call])
