from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from backend.database.base import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)

    description = Column(String(1000))

    github_url = Column(String(500))

    status = Column(String(50), default="NEW")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )