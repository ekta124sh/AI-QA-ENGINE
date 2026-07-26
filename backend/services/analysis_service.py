from sqlalchemy.orm import Session

from backend.database.analysis_crud import save_analysis
from backend.agents.analysis_agent import AnalysisAgent


class AnalysisService:

    @staticmethod
    def analyze_failure(
        db: Session,
        project_id: int,
        execution_id: int,
        test_case: str,
        playwright_script: str,
        error_log: str,
    ):

        print("\n===================================")
        print("AI FAILURE ANALYSIS STARTED")
        print("===================================\n")

        analysis = AnalysisAgent.analyze(
            test_case=test_case,
            playwright_code=playwright_script,
            error_log=error_log,
        )

        save_analysis(
            db=db,
            project_id=project_id,
            execution_id=execution_id,
            analysis=analysis,
        )

        print("AI Analysis Saved Successfully\n")