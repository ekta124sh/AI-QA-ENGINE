from sqlalchemy import Column, Integer, ForeignKey, Text

from backend.database.connection import Base


class PlaywrightTest(Base):

    __tablename__ = "playwright_tests"

    id = Column(Integer, primary_key=True, index=True)

    project_id = Column(
        Integer,
        ForeignKey("projects.id")
    )

    file_name = Column(Text)

    chunk_number = Column(Integer)

    manual_test_case = Column(Text)

    script = Column(Text)