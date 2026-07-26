from sqlalchemy import Column, Integer, String, ForeignKey, Text
from backend.database.base import Base


class TestCase(Base):
    __tablename__ = "test_cases"

    id = Column(Integer, primary_key=True, index=True)

    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)

    file_name = Column(String(255), nullable=False)

    chunk_number = Column(Integer, nullable=False)

    title = Column(String(500), nullable=False)

    module = Column(String(255))

    priority = Column(String(50))

    severity = Column(String(50))

    test_type = Column(String(100))

    preconditions = Column(Text)

    steps = Column(Text)  # JSON string

    expected_result = Column(Text)