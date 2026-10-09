import hashlib

import asyncpg
from pgvector.asyncpg import register_vector

from app.provider import ModelProvider
from app.schemas import PositionInput


def position_text(position: PositionInput) -> str:
    return " ".join([position.company, position.title, position.description, position.education, position.address])[:8000]


class PositionIndex:
    """Persistent hybrid job retrieval backed by PostgreSQL FTS and pgvector."""

    def __init__(self, database_url: str):
        self.database_url = database_url
        self.pool: asyncpg.Pool | None = None

    async def connect(self) -> None:
        self.pool = await asyncpg.create_pool(self.database_url, init=register_vector, min_size=1, max_size=5)

    async def close(self) -> None:
        if self.pool:
            await self.pool.close()
            self.pool = None

    async def sync(self, positions: list[PositionInput], provider: ModelProvider) -> None:
        if not self.pool:
            raise RuntimeError("position index is not connected")
        rows = [(position, position_text(position)) for position in positions]
        hashes = {position.position_id: hashlib.sha256(content.encode("utf-8")).hexdigest() for position, content in rows}
        existing_rows = await self.pool.fetch(
            "SELECT position_id, content_hash FROM position_embeddings WHERE position_id = ANY($1::bigint[])",
            list(hashes),
        )
        existing = {row["position_id"]: row["content_hash"] for row in existing_rows}
        changed = [(position, content) for position, content in rows if existing.get(position.position_id) != hashes[position.position_id]]
        if not changed:
            return
        embeddings = await provider.embed([content for _, content in changed])
        async with self.pool.acquire() as connection:
            async with connection.transaction():
                await connection.executemany(
                    """
                    INSERT INTO position_embeddings(position_id, content, content_hash, embedding, updated_at)
                    VALUES($1, $2, $3, $4, now())
                    ON CONFLICT(position_id) DO UPDATE SET
                      content = EXCLUDED.content,
                      content_hash = EXCLUDED.content_hash,
                      embedding = EXCLUDED.embedding,
                      updated_at = now()
                    """,
                    [(position.position_id, content, hashes[position.position_id], embedding) for (position, content), embedding in zip(changed, embeddings, strict=True)],
                )

    async def search(self, query: str, query_embedding: list[float], limit: int) -> list[int]:
        if not self.pool:
            raise RuntimeError("position index is not connected")
        rows = await self.pool.fetch(
            """
            WITH vector_hits AS (
              SELECT position_id, row_number() OVER (ORDER BY embedding <=> $1) AS rank
              FROM position_embeddings WHERE embedding IS NOT NULL ORDER BY embedding <=> $1 LIMIT $3
            ), text_hits AS (
              SELECT position_id, row_number() OVER (
                ORDER BY ts_rank_cd(to_tsvector('simple', content), plainto_tsquery('simple', $2)) DESC
              ) AS rank
              FROM position_embeddings
              WHERE to_tsvector('simple', content) @@ plainto_tsquery('simple', $2)
              ORDER BY ts_rank_cd(to_tsvector('simple', content), plainto_tsquery('simple', $2)) DESC LIMIT $3
            )
            SELECT COALESCE(v.position_id, t.position_id) AS position_id,
                   COALESCE(1.0 / (60 + v.rank), 0) + COALESCE(1.0 / (60 + t.rank), 0) AS rrf_score
            FROM vector_hits v FULL OUTER JOIN text_hits t USING(position_id)
            ORDER BY rrf_score DESC LIMIT $3
            """,
            query_embedding,
            query,
            limit,
        )
        return [row["position_id"] for row in rows]
