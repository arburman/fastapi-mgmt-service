import os
from pydantic_settings import BaseSettings, SettingsConfigDict

pydantic_env = os.getenv("ENVIRONMENT", "dev").lower()
env_file_path = f".env.{pydantic_env}"

class Settings(BaseSettings):
    APP_NAME: str = "fastapi-mgmt-service"
    API_KEY: str
    WEATHER_API_KEY: str | None = None
    OPENAI_API_KEY: str | None = None
    MAX_SUMMARY_LENGTH: int = 2000

    model_config = SettingsConfigDict(
        env_file=env_file_path,
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()
