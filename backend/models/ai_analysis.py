from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func

from backend.database.base import Base


class AIAnalysis(Base):

    __tablename__ = "ai_analysis"

    id = Column(Integer, primary_key=True, index=True)

    project_id = Column(Integer)

    execution_id = Column(Integer)

    analysis = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )