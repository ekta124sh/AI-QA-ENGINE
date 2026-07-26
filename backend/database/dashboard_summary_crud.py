from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.project import Project
from backend.models.test_case import TestCase
from backend.models.playwright_test import PlaywrightTest
from backend.models.execution_result import ExecutionResult


def get_platform_summary(db: Session):
    """
    Returns overall platform statistics.
    """

    total_projects = db.query(func.count(Project.id)).scalar() or 0

    total_manual_tests = db.query(
        func.count(TestCase.id)
    ).scalar() or 0

    total_playwright_tests = db.query(
        func.count(PlaywrightTest.id)
    ).scalar() or 0

    total_executions = db.query(
        func.count(ExecutionResult.id)
    ).scalar() or 0

    total_passed = db.query(
        func.count(ExecutionResult.id)
    ).filter(
        ExecutionResult.status == "PASS"
    ).scalar() or 0

    total_failed = db.query(
        func.count(ExecutionResult.id)
    ).filter(
        ExecutionResult.status == "FAIL"
    ).scalar() or 0

    return {
        "total_projects": total_projects,
        "total_manual_tests": total_manual_tests,
        "total_playwright_tests": total_playwright_tests,
        "total_executions": total_executions,
        "total_passed": total_passed,
        "total_failed": total_failed,
    }