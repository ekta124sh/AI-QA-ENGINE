import json
import os
import shutil
import subprocess
import tempfile
import time
import sys

from sqlalchemy.orm import Session

from backend.config.settings import settings
from backend.database.connection import SessionLocal
from backend.database.execution_crud import save_execution_result
from backend.models.playwright_test import PlaywrightTest


class ExecutionService:

    @staticmethod
    def execute(project_id: int):

        db: Session = SessionLocal()

        try:

            tests = (
                db.query(PlaywrightTest)
                .filter(
                    PlaywrightTest.project_id == project_id
                )
                .all()
            )

            print(f"\nFound {len(tests)} Playwright Tests")

            if not tests:
                print("No Playwright tests found.")
                return

            # =====================================================
            # Report Directories
            # =====================================================

            project_report_dir = os.path.join(
                "reports",
                f"project_{project_id}"
            )

            allure_results = os.path.join(
                project_report_dir,
                "allure-results"
            )

            allure_report = os.path.join(
                project_report_dir,
                "allure-report"
            )

            os.makedirs(project_report_dir, exist_ok=True)

            if os.path.exists(allure_results):
                shutil.rmtree(allure_results)

            if os.path.exists(allure_report):
                shutil.rmtree(allure_report)

            os.makedirs(allure_results, exist_ok=True)
            os.makedirs(allure_report, exist_ok=True)

            # =====================================================
            # Execute Every Playwright Test
            # =====================================================

            for test in tests:

                print("=" * 80)
                print(f"Executing Chunk {test.chunk_number}")
                print("=" * 80)

                with tempfile.TemporaryDirectory() as temp_dir:

                    script_path = os.path.join(
                        temp_dir,
                        f"test_chunk_{test.chunk_number}.py"
                    )

                    script = test.script.strip()

                    # ---------------------------------------------
                    # Remove Markdown
                    # ---------------------------------------------

                    if script.startswith("```python"):
                        script = script.replace("```python", "", 1)

                    if script.startswith("```"):
                        script = script.replace("```", "", 1)

                    if script.endswith("```"):
                        script = script[:-3]

                    script = script.strip()

                    # ---------------------------------------------
                    # Extract code if stored as JSON
                    # ---------------------------------------------

                    try:
                        parsed = json.loads(script)

                        if isinstance(parsed, list):
                            if parsed and "code" in parsed[0]:
                                script = parsed[0]["code"]

                        elif isinstance(parsed, dict):
                            if "code" in parsed:
                                script = parsed["code"]

                    except Exception:
                        pass

                    script = script.strip()

                    # ---------------------------------------------
                    # Save Temporary Test File
                    # ---------------------------------------------

                    with open(
                        script_path,
                        "w",
                        encoding="utf-8"
                    ) as f:
                        f.write(script)

                    print("\nGenerated Test Script\n")
                    print(script)
                    print("-" * 80)

                    start = time.time()

                    result = subprocess.run(
                        [
                            sys.executable,
                            "-m",
                            "pytest",
                            script_path,
                            "-v",
                            f"--alluredir={allure_results}",
                        ],
                        capture_output=True,
                        text=True,
                    )

                    end = time.time()

                    print("\n========== PYTEST STDOUT ==========\n")
                    print(result.stdout)

                    print("\n========== PYTEST STDERR ==========\n")
                    print(result.stderr)

                    status = (
                        "PASS"
                        if result.returncode == 0
                        else "FAIL"
                    )

                    execution_time = f"{end-start:.2f} sec"

                    save_execution_result(
                        db=db,
                        project_id=project_id,
                        file_name=test.file_name,
                        status=status,
                        execution_time=execution_time,
                        report_path=allure_report,
                    )

                    print("-" * 80)
                    print(f"Status : {status}")
                    print(f"Time   : {execution_time}")
                    print("-" * 80)

            # =====================================================
            # Generate Allure Report
            # =====================================================

            print("\nGenerating Allure Report...\n")

            result = subprocess.run(
                [
                    settings.ALLURE_PATH,
                    "generate",
                    allure_results,
                    "-o",
                    allure_report,
                    "--clean",
                ],
                capture_output=True,
                text=True,
            )

            print("\n========== ALLURE STDOUT ==========\n")
            print(result.stdout)

            print("\n========== ALLURE STDERR ==========\n")
            print(result.stderr)

            print("=" * 80)
            print("Execution Completed Successfully")
            print("=" * 80)
            print(f"Allure Report : {allure_report}")

        finally:
            db.close()