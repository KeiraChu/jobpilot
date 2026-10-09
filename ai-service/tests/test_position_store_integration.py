import asyncio
import os

import pytest

from app.position_store import PositionIndex
from app.schemas import PositionInput


class FakeEmbeddingProvider:
    async def embed(self, texts):
        vectors = []
        for text in texts:
            vector = [0.0] * 1024
            if "RAG" in text or "Python" in text:
                vector[0] = 1.0
            if "会计" in text:
                vector[1] = 1.0
            vectors.append(vector)
        return vectors


def test_pgvector_and_full_text_retrieve_candidates():
    database_url = os.getenv("TEST_POSITION_DATABASE_URL")
    if not database_url:
        pytest.skip("set TEST_POSITION_DATABASE_URL to run the pgvector integration test")

    async def scenario():
        index = PositionIndex(database_url)
        await index.connect()
        try:
            positions = [
                PositionInput(position_id=900001, company="A", title="AI 应用开发", description="Python FastAPI RAG"),
                PositionInput(position_id=900002, company="B", title="财务实习生", description="会计报表与审计"),
            ]
            provider = FakeEmbeddingProvider()
            await index.sync(positions, provider)
            query = "Python RAG 应用开发"
            query_embedding = (await provider.embed([query]))[0]
            result = await index.search(query, query_embedding, 2)
            assert result[0] == 900001
        finally:
            await index.close()

    asyncio.run(scenario())
