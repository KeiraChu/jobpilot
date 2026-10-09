CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS position_embeddings (
  position_id BIGINT PRIMARY KEY, content TEXT NOT NULL, content_hash CHAR(64) NOT NULL DEFAULT '', skills JSONB NOT NULL DEFAULT '[]',
  embedding vector(1024), updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
ALTER TABLE position_embeddings ADD COLUMN IF NOT EXISTS content_hash CHAR(64) NOT NULL DEFAULT '';
CREATE INDEX IF NOT EXISTS idx_position_embedding ON position_embeddings USING hnsw (embedding vector_cosine_ops);
CREATE INDEX IF NOT EXISTS idx_position_content_fts ON position_embeddings USING gin (to_tsvector('simple', content));
CREATE TABLE IF NOT EXISTS ai_runs (
  run_id UUID PRIMARY KEY, user_id VARCHAR(64) NOT NULL, workflow VARCHAR(64) NOT NULL,
  status VARCHAR(32) NOT NULL, model VARCHAR(128), latency_ms INTEGER,
  input_tokens INTEGER, output_tokens INTEGER, embedding_tokens INTEGER, estimated_cost NUMERIC(12,6),
  stage_latency JSONB NOT NULL DEFAULT '{}'::jsonb, fallback_reasons JSONB NOT NULL DEFAULT '[]'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
ALTER TABLE ai_runs ADD COLUMN IF NOT EXISTS embedding_tokens INTEGER;
ALTER TABLE ai_runs ADD COLUMN IF NOT EXISTS estimated_cost NUMERIC(12,6);
ALTER TABLE ai_runs ADD COLUMN IF NOT EXISTS stage_latency JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE ai_runs ADD COLUMN IF NOT EXISTS fallback_reasons JSONB NOT NULL DEFAULT '[]'::jsonb;
