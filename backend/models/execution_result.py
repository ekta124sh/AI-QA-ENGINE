from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from backend.database.base import Base


class ExecutionResult(Base):

    __tablename__ = "execution_results"

    id = Column(Integer, primary_key=True, index=True)

    project_id = Column(Integer)

    file_name = Column(String)

    status = Column(String)

    execution_time = Column(String)

    report_path = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )