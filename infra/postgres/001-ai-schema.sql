CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS position_embeddings (
  position_id BIGINT PRIMARY KEY, content TEXT NOT NULL, skills JSONB NOT NULL DEFAULT '[]',
  embedding vector(1024), updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_position_embedding ON position_embeddings USING hnsw (embedding vector_cosine_ops);
CREATE INDEX IF NOT EXISTS idx_position_content_fts ON position_embeddings USING gin (to_tsvector('simple', content));
CREATE TABLE IF NOT EXISTS ai_runs (
  run_id UUID PRIMARY KEY, user_id VARCHAR(64) NOT NULL, workflow VARCHAR(64) NOT NULL,
  status VARCHAR(32) NOT NULL, model VARCHAR(128), latency_ms INTEGER,
  input_tokens INTEGER, output_tokens INTEGER, created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
