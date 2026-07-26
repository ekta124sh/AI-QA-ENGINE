from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.project import Project
from backend.models.test_case import TestCase
from backend.models.playwright_test import PlaywrightTest
from backend.models.execution_result import ExecutionResult


# =====================================================
# Dashboard Summary
# =====================================================

def get_report_summary(db: Session):

    total_projects = db.query(func.count(Project.id)).scalar()

    total_test_cases = db.query(
        func.count(TestCase.id)
    ).scalar()

    total_playwright = db.query(
        func.count(PlaywrightTest.id)
    ).scalar()

    if total_test_cases == 0:
        coverage = 0
    else:
        coverage = round(
            (total_playwright / total_test_cases) * 100,
            2,
        )

        # Coverage should never exceed 100%
        coverage = min(coverage, 100)

    return {
        "total_projects": total_projects,
        "total_test_cases": total_test_cases,
        "total_playwright_scripts": total_playwright,
        "automation_coverage": coverage,
    }


# =====================================================
# Priority Distribution
# =====================================================

def get_priority_distribution(db: Session):

    results = (
        db.query(
            TestCase.priority,
            func.count(TestCase.id)
        )
        .group_by(TestCase.priority)
        .all()
    )

    return [
        {
            "priority": priority if priority else "Unknown",
            "count": count,
        }
        for priority, count in results
    ]


# =====================================================
# Severity Distribution
# =====================================================

def get_severity_distribution(db: Session):

    results = (
        db.query(
            TestCase.severity,
            func.count(TestCase.id)
        )
        .group_by(TestCase.severity)
        .all()
    )

    return [
        {
            "severity": severity if severity else "Unknown",
            "count": count,
        }
        for severity, count in results
    ]


# =====================================================
# Test Type Distribution
# =====================================================

def get_test_type_distribution(db: Session):

    results = (
        db.query(
            TestCase.test_type,
            func.count(TestCase.id)
        )
        .group_by(TestCase.test_type)
        .all()
    )

    return [
        {
            "test_type": test_type if test_type else "Unknown",
            "count": count,
        }
        for test_type, count in results
    ]


# =====================================================
# Project Wise Test Cases
# =====================================================

def get_project_distribution(db: Session):

    results = (
        db.query(
            Project.name,
            func.count(TestCase.id)
        )
        .outerjoin(
            TestCase,
            Project.id == TestCase.project_id
        )
        .group_by(Project.name)
        .all()
    )

    return [
        {
            "project": project,
            "test_cases": count,
        }
        for project, count in results
    ]