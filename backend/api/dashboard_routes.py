from fastapi import APIRouter, HTTPException, Depends

from backend.auth.dependencies import get_current_user
from backend.models.user import User

from backend.services.dashboard_summary_service import (
    DashboardSummaryService,
)

from backend.services.dashboard_service import DashboardService

from backend.services.execution_history_service import (
    ExecutionHistoryService,
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


# ==========================================================
# Platform Dashboard Summary
# ==========================================================

@router.get("/summary")
def get_dashboard_summary(
    current_user: User = Depends(get_current_user),
):
    """
    Returns overall platform statistics.
    """

    return DashboardSummaryService.get_summary()


# ==========================================================
# Project Dashboard Summary
# ==========================================================

@router.get("/project/{project_id}")
def get_dashboard(
    project_id: int,
    current_user: User = Depends(get_current_user),
):
    """
    Returns dashboard summary for a specific project.
    """

    summary = DashboardService.get_summary(project_id)

    if summary.get("error"):
        raise HTTPException(
            status_code=404,
            detail=summary["error"],
        )

    return summary


# ==========================================================
# Project Execution History
# ==========================================================

@router.get("/project/{project_id}/executions")
def get_execution_history(
    project_id: int,
    current_user: User = Depends(get_current_user),
):
    """
    Returns execution history for a specific project.
    """

    return ExecutionHistoryService.get_history(project_id)