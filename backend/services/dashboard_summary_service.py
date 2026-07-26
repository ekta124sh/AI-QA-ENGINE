from sqlalchemy.orm import Session

from backend.database.connection import SessionLocal
from backend.database.dashboard_summary_crud import (
    get_platform_summary,
)


class DashboardSummaryService:

    @staticmethod
    def get_summary():

        db: Session = SessionLocal()

        try:

            summary = get_platform_summary(db)

            total = (
                summary["total_passed"]
                + summary["total_failed"]
            )

            if total == 0:
                pass_rate = 0
            else:
                pass_rate = round(
                    (summary["total_passed"] / total) * 100,
                    2,
                )

            summary["overall_pass_rate"] = pass_rate

            return summary

        finally:
            db.close()