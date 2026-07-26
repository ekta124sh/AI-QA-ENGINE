from fastapi import APIRouter, Depends

from backend.auth.dependencies import get_current_user
from backend.models.user import User

from backend.database.connection import SessionLocal
from backend.database.execution_crud import get_execution_summary
from backend.database.execution_history_crud import get_execution_history
from backend.services.execution_service import ExecutionService

router = APIRouter(
    prefix="/execute",
    tags=["Execution"],
)


@router.post("/{project_id}")
def execute(
    project_id: int,
    current_user: User = Depends(get_current_user),
):
    """
    Execute Playwright tests for a project.
    Authentication required.
    """

    ExecutionService.execute(project_id)

    return {
        "message": "Execution Completed"
    }


@router.get("/{project_id}/summary")
def execution_summary(
    project_id: int,
    current_user: User = Depends(get_current_user),
):
    """
    Get execution summary.
    Authentication required.
    """

    db = SessionLocal()

    try:
        return get_execution_summary(
            db=db,
            project_id=project_id
        )
    finally:
        db.close()


@router.get("/{project_id}/history")
def execution_history(
    project_id: int,
    current_user: User = Depends(get_current_user),
):
    """
    Get execution history.
    Authentication required.
    """

    db = SessionLocal()

    try:
        return get_execution_history(
            db=db,
            project_id=project_id
        )
    finally:
        db.close()