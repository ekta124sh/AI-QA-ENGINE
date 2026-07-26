from fastapi import APIRouter, Depends

from backend.auth.dependencies import get_current_user
from backend.models.user import User
from backend.services.playwright_service import PlaywrightService

router = APIRouter(
    prefix="/playwright",
    tags=["Playwright"],
)


@router.post("/{project_id}")
def generate_playwright(
    project_id: int,
    current_user: User = Depends(get_current_user),
):
    """
    Generate Playwright test scripts for a project.
    Authentication required.
    """

    PlaywrightService.generate(project_id)

    return {
        "message": "Playwright tests generated successfully."
    }


@router.get("/{project_id}")
def get_playwright(
    project_id: int,
    current_user: User = Depends(get_current_user),
):
    """
    Get generated Playwright scripts.
    Authentication required.
    """

    return PlaywrightService.get_playwright_tests(project_id)