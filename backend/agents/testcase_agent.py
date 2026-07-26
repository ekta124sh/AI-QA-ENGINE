from backend.ai.engine.ai_engine import AIEngine
from backend.ai.models.ai_request import AIRequest
from backend.ai.types.ai_task import AITask

from backend.generators.testcase_formatter import TestCaseFormatter
from backend.prompts.prompt_builder import build_testcase_prompt


class TestCaseAgent:
    """
    AI Agent responsible for generating manual API test cases.
    """

    @staticmethod
    def generate(
        repository_context: dict,
        file_name: str,
        chunk: str,
    ):

        prompt = build_testcase_prompt(
            repository_context=repository_context,
            file_name=file_name,
            code=chunk,
        )

        request = AIRequest(
            task=AITask.TESTCASE,
            prompt=prompt,
        )

        response = AIEngine.execute(request)

        print("=" * 80)
        print("RAW AI RESPONSE")
        print("=" * 80)
        print(response.content)
        print("=" * 80)

        if not response.success:
            raise Exception(response.error)

        print("=" * 80)
        print("FORMATTING AI RESPONSE")
        print("=" * 80)

        try:

            testcases = TestCaseFormatter.format(
                response.content
            )

            print(f"Generated {len(testcases)} valid test cases.")

            return testcases

        except Exception as ex:

            print("=" * 80)
            print("FAILED TO PARSE LLM RESPONSE")
            print("=" * 80)
            print(str(ex))
            print("=" * 80)

            print("\nRAW RESPONSE\n")
            print(response.content)

            raise