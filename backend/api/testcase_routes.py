from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.auth.dependencies import get_current_user
from backend.database.dependencies import get_db
from backend.database.testcase_crud import get_testcases
from backend.models.user import User
from backend.schemas.test_case import TestCaseResponse

router = APIRouter(
    prefix="/testcases",
    tags=["Test Cases"]
)


@router.get(
    "/{project_id}",
    response_model=list[TestCaseResponse],
)
def list_testcases(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Get all generated test cases for a project.
    Authentication required.
    """

    records = get_testcases(db, project_id)

    return records