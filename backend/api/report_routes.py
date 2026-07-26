import os

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse, RedirectResponse
from sqlalchemy.orm import Session

from backend.auth.dependencies import get_current_user
from backend.models.user import User

from backend.database.dependencies import get_db
from backend.database.testcase_crud import get_testcases

from backend.reports.excel_report import generate_excel
from backend.reports.pdf_report import generate_pdf
from backend.database.report_crud import get_report_summary

from backend.database.report_crud import (
    get_report_summary,
    get_priority_distribution,
    get_severity_distribution,
    get_test_type_distribution,
    get_project_distribution,
)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


# =====================================================
# Reports Summary
# =====================================================

@router.get("/summary")
def report_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_report_summary(db)


# =====================================================
# Priority Distribution
# =====================================================

@router.get("/priority")
def priority_distribution(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_priority_distribution(db)


# =====================================================
# Severity Distribution
# =====================================================

@router.get("/severity")
def severity_distribution(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_severity_distribution(db)


# =====================================================
# Test Type Distribution
# =====================================================

@router.get("/test-types")
def test_type_distribution(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_test_type_distribution(db)


# =====================================================
# Project Distribution
# =====================================================

@router.get("/projects")
def project_distribution(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_project_distribution(db)

# =====================================================
# Excel Report
# =====================================================

@router.get("/project/{project_id}/excel")
def export_excel(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    testcases = get_testcases(db, project_id)

    if not testcases:
        return {
            "error": "No test cases found."
        }

    os.makedirs("generated_reports", exist_ok=True)

    filename = f"generated_reports/project_{project_id}.xlsx"

    generate_excel(
        testcases,
        filename
    )

    return FileResponse(
        filename,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=f"AI_TestCases_Project_{project_id}.xlsx"
    )


# =====================================================
# PDF Report
# =====================================================

@router.get("/project/{project_id}/pdf")
def export_pdf(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    testcases = get_testcases(db, project_id)

    if not testcases:
        return {
            "error": "No test cases found."
        }

    os.makedirs("generated_reports", exist_ok=True)

    filename = f"generated_reports/project_{project_id}.pdf"

    generate_pdf(
        testcases,
        filename
    )

    return FileResponse(
        filename,
        media_type="application/pdf",
        filename=f"AI_TestCases_Project_{project_id}.pdf"
    )


# =====================================================
# Allure Report
# =====================================================

@router.get("/project/{project_id}/allure")
def open_allure_report(
    project_id: int,
    current_user: User = Depends(get_current_user),
):
    report_folder = os.path.join(
        "reports",
        f"project_{project_id}",
        "allure-report"
    )

    index_file = os.path.join(
        report_folder,
        "index.html"
    )

    if not os.path.exists(index_file):
        raise HTTPException(
            status_code=404,
            detail="Allure report not found."
        )

    return RedirectResponse(
        url=f"/allure/project_{project_id}/allure-report/index.html"
    )