"""Application configuration using pydantic-settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_env: str = "development"
    app_name: str = "Real Estate Lead Bot"
    app_version: str = "0.1.0"
    debug: bool = True

    database_url: str = "postgresql://postgres:postgres@localhost:5432/real_estate_leads"

    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 60

    cors_origins: str = "http://localhost:3000,http://localhost:5173"

    n8n_webhook_url: str = "http://localhost:5678/webhook"
    n8n_webhook_secret: str = ""

    ai_api_key: str = ""
    ai_model: str = "gpt-4o-mini"
    ai_base_url: str = ""

    log_level: str = "INFO"


settings = Settings()
