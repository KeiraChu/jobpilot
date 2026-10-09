from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="AI_", env_file=".env", extra="ignore")
    environment: str = "development"
    internal_api_key: str = "change-me"
    api_key: str = ""
    model_base_url: str = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    chat_model: str = "qwen-plus"
    embedding_model: str = "text-embedding-v4"
    timeout_seconds: float = 45
    max_retries: int = 2
    top_k: int = 10
    rerank_candidates: int = 8
    database_url: str = "postgresql://jobpilot:jobpilot@localhost:5432/jobpilot_ai"
    use_position_index: bool = True


@lru_cache
def get_settings() -> Settings:
    return Settings()
