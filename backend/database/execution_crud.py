from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.execution_result import ExecutionResult


def save_execution_result(
    db: Session,
    project_id: int,
    file_name: str,
    status: str,
    execution_time: str,
    report_path: str,
):

    result = ExecutionResult(
        project_id=project_id,
        file_name=file_name,
        status=status,
        execution_time=execution_time,
        report_path=report_path,
    )

    db.add(result)
    db.commit()
    db.refresh(result)

    return result


def get_execution_summary(
    db: Session,
    project_id: int,
):

    total_tests = (
        db.query(ExecutionResult)
        .filter(
            ExecutionResult.project_id == project_id
        )
        .count()
    )

    passed = (
        db.query(ExecutionResult)
        .filter(
            ExecutionResult.project_id == project_id,
            ExecutionResult.status == "PASS"
        )
        .count()
    )

    failed = (
        db.query(ExecutionResult)
        .filter(
            ExecutionResult.project_id == project_id,
            ExecutionResult.status == "FAIL"
        )
        .count()
    )

    latest = (
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
        "project_id": project_id,
        "total_tests": total_tests,
        "passed": passed,
        "failed": failed,
        "status": "Completed" if total_tests > 0 else "Not Executed",
        "last_execution": (
            latest.created_at.strftime("%d-%m-%Y %H:%M:%S")
            if latest
            else None
        ),
    }