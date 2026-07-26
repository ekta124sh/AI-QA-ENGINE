from fastapi import APIRouter
from fastapi.responses import FileResponse

from backend.database.connection import SessionLocal
from backend.reports.playwright_export import export_playwright

router = APIRouter(
    prefix="/playwright",
    tags=["Playwright Export"]
)


@router.get("/{project_id}/download")
def download(project_id: int):

    db = SessionLocal()

    try:

        filename = export_playwright(project_id, db)

        return FileResponse(
            filename,
            media_type="application/zip",
            filename=f"project_{project_id}_playwright.zip",
        )

    finally:
        db.close()