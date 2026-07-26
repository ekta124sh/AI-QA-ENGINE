from backend.llm.factory import get_llm
from backend.prompts.analysis_prompt import build_analysis_prompt


class AnalysisAgent:

    @staticmethod
    def analyze(
        test_case: str,
        playwright_code: str,
        error_log: str,
    ):

        prompt = build_analysis_prompt(
            test_case,
            playwright_code,
            error_log,
        )

        llm = get_llm()

        return llm.generate(prompt)