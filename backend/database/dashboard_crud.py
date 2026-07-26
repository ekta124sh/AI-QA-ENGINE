from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.project import Project
from backend.models.test_case import TestCase
from backend.models.playwright_test import PlaywrightTest
from backend.models.execution_result import ExecutionResult


def get_dashboard_summary(
    db: Session,
    project_id: int,
):
    """
    Returns dashboard statistics for a project.
    """

    project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    if not project:
        return None

    manual_tests = (
        db.query(func.count(TestCase.id))
        .filter(TestCase.project_id == project_id)
        .scalar()
    )

    playwright_tests = (
        db.query(func.count(PlaywrightTest.id))
        .filter(PlaywrightTest.project_id == project_id)
        .scalar()
    )

    executions = (
        db.query(func.count(ExecutionResult.id))
        .filter(ExecutionResult.project_id == project_id)
        .scalar()
    )

    passed = (
        db.query(func.count(ExecutionResult.id))
        .filter(
            ExecutionResult.project_id == project_id,
            ExecutionResult.status == "PASS",
        )
        .scalar()
    )

    failed = (
        db.query(func.count(ExecutionResult.id))
        .filter(
            ExecutionResult.project_id == project_id,
            ExecutionResult.status == "FAIL",
        )
        .scalar()
    )

    latest_execution = (
        db.query(ExecutionResult)
        .filter(
            ExecutionResult.project_id == project_id
        )
        .order_by(
            ExecutionResult.created_at.desc()
        )
        .first()
    )

    return {
        "project_name": project.name,
        "github_url": project.github_url,
        "manual_testcases": manual_tests,
        "playwright_tests": playwright_tests,
        "executions": executions,
        "passed": passed,
        "failed": failed,
        "last_execution": (
            latest_execution.created_at
            if latest_execution
            else None
        ),
    }