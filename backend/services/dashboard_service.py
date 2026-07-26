from sqlalchemy.orm import Session

from backend.database.connection import SessionLocal
from backend.database.dashboard_crud import get_dashboard_summary


class DashboardService:

    @staticmethod
    def get_summary(project_id: int):

        db: Session = SessionLocal()

        try:

            summary = get_dashboard_summary(
                db=db,
                project_id=project_id,
            )

            if summary is None:
                return {
                    "error": "Project not found."
                }

            # ----------------------------
            # Calculate Pass Rate
            # ----------------------------

            total = summary["passed"] + summary["failed"]

            if total == 0:
                pass_rate = 0
            else:
                pass_rate = round(
                    (summary["passed"] / total) * 100,
                    2,
                )

            summary["pass_rate"] = pass_rate

            # ----------------------------
            # Report URLs
            # ----------------------------

            summary["allure_report"] = (
                f"/reports/project/{project_id}/allure"
            )

            summary["excel_report"] = (
                f"/reports/project/{project_id}/excel"
            )

            summary["pdf_report"] = (
                f"/reports/project/{project_id}/pdf"
            )

            return summary

        finally:

            db.close()