from backend.ai.engine.ai_engine import AIEngine

from backend.ai.models.ai_request import AIRequest
from backend.ai.models.ai_response import AIResponse
from backend.ai.types.ai_task import AITask

from backend.prompts.playwright_prompt import build_playwright_prompt

from backend.utils.playwright_cleaner import PlaywrightCleaner
from backend.utils.playwright_validator import PlaywrightValidator


class PlaywrightAgent:

    @staticmethod
    def generate(
        project_context: str,
        repository_context: str,
        manual_test_case: str,
    ):

        ai_context = f"""
PROJECT CONTEXT

{project_context}

==================================================

REPOSITORY CONTEXT

{repository_context}

==================================================

MANUAL TEST CASE

{manual_test_case}
"""

        prompt = build_playwright_prompt(ai_context)

        request = AIRequest(
            task=AITask.PLAYWRIGHT,
            prompt=prompt,
        )

        response = AIEngine.execute(request)

        if not response.success:
            raise Exception(response.error)

        # ----------------------------------------------------
        # RAW RESPONSE
        # ----------------------------------------------------
        print("\n" + "=" * 80)
        print("RAW AI RESPONSE")
        print("=" * 80)

        print(response.content)

        print("=" * 80)

        code = PlaywrightCleaner.clean(
            response.content
        )

        print("\n" + "=" * 80)
        print("CLEANED CODE")
        print("=" * 80)

        print(code)

        print("=" * 80)

        errors = PlaywrightValidator.validate(code)

        if errors:

            print("\nVALIDATION ERRORS")

            for err in errors:
                print("-", err)

            raise Exception("\n".join(errors))

        return code