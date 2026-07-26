from sqlalchemy.orm import Session
from pathlib import Path

from backend.services.git_service import GitService

from backend.utils.file_scanner import scan_repository
from backend.utils.code_loader import load_code
from backend.utils.code_chunker import chunk_code

from backend.analyzers.repository_analyzer import RepositoryAnalyzer
from backend.context.repository_context import RepositoryContext
from backend.context.endpoint_context import EndpointContext

from backend.database.connection import SessionLocal
from backend.database.testcase_crud import (
    create_testcase,
    delete_testcases,
)

from backend.agents.testcase_agent import TestCaseAgent


class PipelineService:

    @staticmethod
    def generate_testcases(project_id: int, repo_url: str):

        db: Session = SessionLocal()

        try:

            print("=" * 70)
            print("STARTING AI TEST CASE GENERATION")
            print("=" * 70)

            # -------------------------------------------------
            # Delete Existing Test Cases
            # -------------------------------------------------

            print("Deleting old test cases...")

            delete_testcases(db, project_id)

            # -------------------------------------------------
            # Clone Repository
            # -------------------------------------------------

            print("Cloning Repository...")

            repo_path = GitService.clone_repository(repo_url)

            print("Repository Ready")

            # -------------------------------------------------
            # Repository Analysis
            # -------------------------------------------------

            print("\nAnalyzing Repository...")

            analysis = RepositoryAnalyzer.analyze(repo_path)

            print("=" * 70)
            print("REPOSITORY ANALYSIS")
            print("=" * 70)

            for key, value in analysis.items():

                if key == "endpoints":
                    print(f"{key} : {len(value)} endpoints")
                else:
                    print(f"{key} : {value}")

            print("=" * 70)

            # -------------------------------------------------
            # Scan Repository
            # -------------------------------------------------

            files = scan_repository(repo_path)

            # Development Mode
            files = files[:1]

            print(f"\nFound {len(files)} files")

            # -------------------------------------------------
            # Process Files
            # -------------------------------------------------

            for file in files:

                print("\n" + "-" * 70)
                print(f"Processing File : {file}")
                print("-" * 70)

                code = load_code(file)

                chunks = chunk_code(code)

                # Development Mode
                chunks = chunks[:2]

                print(f"Chunks Found : {len(chunks)}")

                file_name = Path(file).name

                # -------------------------------------------------
                # Build Repository Context
                # -------------------------------------------------

                repository_context = RepositoryContext.build(
                    analysis=analysis,
                    current_file=file,
                )

                endpoint_count = len(repository_context["endpoints"])

                print(f"Relevant Endpoints : {endpoint_count}")

                # =================================================
                # ENDPOINT-WISE GENERATION
                # =================================================

                if endpoint_count > 0:

                    print("\nGenerating endpoint-wise test cases...")

                    for endpoint in repository_context["endpoints"][:1]:

                        print("\n" + "=" * 70)
                        print(
                            f"Endpoint : {endpoint.get('method')} "
                            f"{endpoint.get('path')}"
                        )
                        print("=" * 70)

                        endpoint_context = EndpointContext.build(
                            repository_context,
                            endpoint,
                        )

                        for index, chunk in enumerate(chunks, start=1):

                            print(f"Generating Chunk {index}")

                            testcases = TestCaseAgent.generate(
                                repository_context=endpoint_context,
                                file_name=file_name,
                                chunk=chunk,
                            )

                            print(
                                f"Generated {len(testcases)} test cases"
                            )

                            for tc in testcases:

                                create_testcase(
                                    db=db,
                                    project_id=project_id,
                                    file_name=file_name,
                                    chunk_number=index,
                                    testcase=tc,
                                )

                    print("\nCompleted endpoint-wise generation.")

                # =================================================
                # FALLBACK
                # =================================================

                else:

                    print(
                        "\nNo endpoints detected."
                        " Using file-level generation."
                    )

                    for index, chunk in enumerate(chunks, start=1):

                        print("\n" + "=" * 70)
                        print(f"Generating Chunk {index}")
                        print("=" * 70)

                        testcases = TestCaseAgent.generate(
                            repository_context=repository_context,
                            file_name=file_name,
                            chunk=chunk,
                        )

                        print(
                            f"Generated {len(testcases)} test cases"
                        )

                        for tc in testcases:

                            create_testcase(
                                db=db,
                                project_id=project_id,
                                file_name=file_name,
                                chunk_number=index,
                                testcase=tc,
                            )

                    print("\nCompleted file-level generation.")

            print("\n" + "=" * 70)
            print("AI TEST CASE GENERATION COMPLETED")
            print("=" * 70)

        except Exception as e:

            print("\nPipeline Failed")
            print(e)
            raise

        finally:

            db.close()