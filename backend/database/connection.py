from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.config.settings import settings
from backend.database.base import Base

# Import all models BEFORE create_all()
from backend.models.project import Project
from backend.models.test_case import TestCase
from backend.models.playwright_test import PlaywrightTest
from backend.models.execution_result import ExecutionResult
from backend.models.ai_analysis import AIAnalysis
from backend.models.user import User


DATABASE_URL = (
    f"postgresql://{settings.DB_USER}:"
    f"{settings.DB_PASSWORD}@"
    f"{settings.DB_HOST}:"
    f"{settings.DB_PORT}/"
    f"{settings.DB_NAME}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Create all database tables
Base.metadata.create_all(bind=engine)