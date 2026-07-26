from sqlalchemy.orm import Session

from backend.database.connection import SessionLocal
from backend.database.execution_history_crud import (
    get_execution_history,
)


class ExecutionHistoryService:

    @staticmethod
    def get_history(project_id: int):

        db: Session = SessionLocal()

        try:

            return get_execution_history(
                db=db,
                project_id=project_id,
            )

        finally:
            db.close()