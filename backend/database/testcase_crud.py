from sqlalchemy.orm import Session
import json

from backend.models.test_case import TestCase


def create_testcase(
    db: Session,
    project_id: int,
    file_name: str,
    chunk_number: int,
    testcase: dict,
):
    # -------------------------------------------------------
    # Normalize Steps
    # -------------------------------------------------------
    steps = testcase.get("steps", [])

    if isinstance(steps, dict):
        # {"1":"step1","2":"step2"} -> ["step1","step2"]
        steps = list(steps.values())

    elif isinstance(steps, str):
        steps = [steps]

    elif not isinstance(steps, list):
        steps = []

    # -------------------------------------------------------
    # Debug
    # -------------------------------------------------------
    print("=" * 80)
    print("BEFORE SAVING TEST CASE")
    print("=" * 80)
    print("Title :", testcase.get("title"))
    print("Steps :", steps)
    print("Type  :", type(steps))
    print("JSON  :", json.dumps(steps, indent=2))
    print("=" * 80)

    db_testcase = TestCase(
        project_id=project_id,
        file_name=file_name,
        chunk_number=chunk_number,

        title=testcase.get("title", ""),
        module=testcase.get("module", ""),
        priority=testcase.get("priority", ""),
        severity=testcase.get("severity", ""),
        test_type=testcase.get("test_type", testcase.get("type", "")),
        preconditions=testcase.get("preconditions", ""),

        # Store JSON string
        steps=json.dumps(steps, indent=2),

        expected_result=testcase.get("expected_result", ""),
    )

    db.add(db_testcase)
    db.commit()
    db.refresh(db_testcase)

    return db_testcase


def get_testcases(db: Session, project_id: int):
    records = (
        db.query(TestCase)
        .filter(TestCase.project_id == project_id)
        .all()
    )

    for tc in records:
        if tc.steps:
            try:
                parsed = json.loads(tc.steps)

                if isinstance(parsed, list):
                    tc.steps = parsed

                elif isinstance(parsed, dict):
                    tc.steps = list(parsed.values())

                elif isinstance(parsed, str):
                    tc.steps = [parsed]

                else:
                    tc.steps = []

            except Exception as ex:
                print(f"Failed to parse steps for TestCase ID {tc.id}: {ex}")
                tc.steps = []
        else:
            tc.steps = []

    return records


def delete_testcases(db: Session, project_id: int):
    (
        db.query(TestCase)
        .filter(TestCase.project_id == project_id)
        .delete()
    )

    db.commit()