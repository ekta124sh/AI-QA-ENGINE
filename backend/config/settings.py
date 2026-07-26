from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ==========================================================
    # Application Settings
    # ==========================================================

    APP_NAME: str = "AI QA Engineer"
    APP_VERSION: str = "1.0.0"

    # ==========================================================
    # LLM Configuration
    # ==========================================================

    LLM_PROVIDER: str = "groq"

    GEMINI_API_KEY: Optional[str] = None
    GROQ_API_KEY: Optional[str] = None
    OPENROUTER_API_KEY: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None

    # ==========================================================
    # Database Configuration
    # ==========================================================

    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "ai_qa_engine"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = ""

    # ==========================================================
    # Allure Configuration
    # ==========================================================

    ALLURE_PATH: str = "allure"

    # ==========================================================
    # Frontend Configuration
    # ==========================================================

    VITE_API_BASE_URL: str = "http://127.0.0.1:8000"

    # ==========================================================
    # Pydantic Settings
    # ==========================================================

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()