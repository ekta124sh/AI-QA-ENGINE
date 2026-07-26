from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.auth.dependencies import get_current_user
from backend.database.dependencies import get_db
from backend.database.crud import (
    create_project,
    get_projects,
    get_project,
)
from backend.models.user import User
from backend.schemas.project import (
    ProjectCreate,
    ProjectResponse,
)
from backend.services.git_service import GitService
from backend.services.pipeline_service import PipelineService

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post("/", response_model=ProjectResponse)
def add_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Create a new project.
    Requires authentication.
    """

    # Save project to PostgreSQL
    new_project = create_project(db, project)

    # Clone GitHub repository
    GitService.clone_repository(project.github_url)

    # Return saved project
    return new_project


@router.get("/", response_model=list[ProjectResponse])
def list_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    List all projects.
    Requires authentication.
    """
    return get_projects(db)


@router.post("/{project_id}/generate-tests")
def generate_tests(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Generate AI test cases for a project.
    Requires authentication.
    """

    project = get_project(db, project_id)

    if not project:
        return {
            "error": "Project not found"
        }

    PipelineService.generate_testcases(
        project.id,
        project.github_url,
    )

    return {
        "message": "Test cases generated successfully",
        "project_id": project.id,
    }