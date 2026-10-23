import os
from pydantic_settings import BaseSettings, SettingsConfigDict

pydantic_env = os.getenv("ENVIRONMENT", "dev").lower()
env_file_path = f".env.{pydantic_env}"

class Settings(BaseSettings):
    API_KEY: str
    APP_NAME: str = "fastapi-mgmt-service"
    MAX_SUMMARY_LENGTH: int = 2000
    OLLAMA_BASE_URL: str | None = None
    OPENAI_API_KEY: str | None = None
    OPENAI_MODEL_SEMVER: str | None = None
    WEATHER_API_KEY: str | None = None

    model_config = SettingsConfigDict(
        env_file=env_file_path,
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()
