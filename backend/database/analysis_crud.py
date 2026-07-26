from sqlalchemy.orm import Session

from backend.models.ai_analysis import AIAnalysis


def save_analysis(
    db: Session,
    project_id: int,
    execution_id: int,
    analysis: str,
):

    item = AIAnalysis(
        project_id=project_id,
        execution_id=execution_id,
        analysis=analysis,
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item