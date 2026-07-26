from sqlalchemy.orm import Session

from backend.models.project import Project
from backend.schemas.project import ProjectCreate


def create_project(db: Session, project: ProjectCreate):

    db_project = Project(
        name=project.name,
        description=project.description,
        github_url=project.github_url,
    )

    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    return db_project


def get_projects(db: Session):
    return db.query(Project).all()

def get_project(db: Session, project_id: int):
    return (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )