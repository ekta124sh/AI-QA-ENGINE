from sqlalchemy.orm import Session

from backend.models.execution_result import ExecutionResult


def get_execution_history(
    db: Session,
    project_id: int,
):
    """
    Returns execution history for a project.
    """

    executions = (
        db.query(ExecutionResult)
        .filter(
            ExecutionResult.project_id == project_id
        )
        .order_by(
            ExecutionResult.created_at.desc()
        )
        .all()
    )

    history = []

    for execution in executions:

        history.append(
            {
                "execution_id": execution.id,
                "file_name": execution.file_name,
                "status": execution.status,
                "execution_time": execution.execution_time,
                "report_path": execution.report_path,
                "created_at": execution.created_at,
            }
        )

    return history