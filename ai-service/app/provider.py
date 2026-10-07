import asyncio
import json

import httpx

from app.config import Settings


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
                return json.loads(response.json()["choices"][0]["message"]["content"])
            except (httpx.HTTPError, KeyError, json.JSONDecodeError) as exc:
                error = exc
                if attempt < self.settings.max_retries:
                    await asyncio.sleep(0.5 * 2**attempt)
        raise RuntimeError("模型服务暂时不可用") from error

    async def close(self):
        await self.client.aclose()

