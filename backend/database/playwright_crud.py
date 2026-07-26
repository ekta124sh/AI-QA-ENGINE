from sqlalchemy.orm import Session

from backend.models.playwright_test import PlaywrightTest


def create_playwright_test(
    db: Session,
    project_id: int,
    file_name: str,
    chunk_number: int,
    manual_test_case: str,
    script: str,
):
    """
    Save generated Playwright script.
    """

    playwright_test = PlaywrightTest(
        project_id=project_id,
        file_name=file_name,
        chunk_number=chunk_number,
        manual_test_case=manual_test_case,
        script=script,
    )

    db.add(playwright_test)
    db.commit()
    db.refresh(playwright_test)

    return playwright_test


def get_playwright_tests(
    db: Session,
    project_id: int,
):
    """
    Fetch all Playwright tests for a project.
    """

    return (
        db.query(PlaywrightTest)
        .filter(
            PlaywrightTest.project_id == project_id
        )
        .order_by(
            PlaywrightTest.chunk_number
        )
        .all()
    )


def delete_playwright_tests(
    db: Session,
    project_id: int,
):
    """
    Delete all existing Playwright tests for a project.
    This avoids duplicate generations.
    """

    (
        db.query(PlaywrightTest)
        .filter(
            PlaywrightTest.project_id == project_id
        )
        .delete(synchronize_session=False)
    )

    db.commit()