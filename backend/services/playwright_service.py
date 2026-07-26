from backend.database.connection import SessionLocal

from backend.database.playwright_crud import (
    create_playwright_test,
    delete_playwright_tests,
    get_playwright_tests,
)

from backend.database.testcase_crud import (
    get_testcases,
)

from backend.llm.factory import get_llm

from backend.prompts.playwright_prompt import (
    build_playwright_prompt,
)


class PlaywrightService:

    @staticmethod
    def generate(project_id: int):
        """
        Generate Playwright scripts from Manual Test Cases.
        """

        db = SessionLocal()

        # Automatically selects provider from .env (Groq/OpenRouter)
        llm = get_llm()

        try:

            # Delete previously generated scripts
            delete_playwright_tests(
                db=db,
                project_id=project_id,
            )

            # Fetch manual test cases
            manual_testcases = get_testcases(
                db=db,
                project_id=project_id,
            )

            if not manual_testcases:
                raise ValueError(
                    f"No manual test cases found for project {project_id}"
                )

            for testcase in manual_testcases:

                manual_test = f"""
Title:
{testcase.title}

Module:
{testcase.module or "General"}

Priority:
{testcase.priority or "Medium"}

Severity:
{testcase.severity or "Medium"}

Test Type:
{testcase.test_type or "Functional"}

Preconditions:
{testcase.preconditions or "None"}

Steps:
{testcase.steps}

Expected Result:
{testcase.expected_result}
"""

                print("=" * 80)
                print(f"Generating Playwright for Test Case #{testcase.id}")
                print("=" * 80)

                prompt = build_playwright_prompt(
                    manual_test
                )

                script = llm.generate(prompt)

                create_playwright_test(
                    db=db,
                    project_id=project_id,
                    file_name=testcase.file_name,
                    chunk_number=testcase.chunk_number,
                    manual_test_case=manual_test,
                    script=script,
                )

            print(f"\nSuccessfully generated {len(manual_testcases)} Playwright scripts.")

        finally:
            db.close()

    @staticmethod
    def get_playwright_tests(project_id: int):

        db = SessionLocal()

        try:

            return get_playwright_tests(
                db=db,
                project_id=project_id,
            )

        finally:
            db.close()