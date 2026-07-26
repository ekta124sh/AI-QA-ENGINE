from pydantic import BaseModel
from typing import List


class TestCaseResponse(BaseModel):
    id: int
    project_id: int
    file_name: str
    chunk_number: int

    title: str
    module: str
    priority: str
    severity: str
    test_type: str
    preconditions: str
    steps: List[str]
    expected_result: str

    class Config:
        from_attributes = True