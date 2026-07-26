from backend.prompts.prompt_builder import (
    build_testcase_prompt,
)

from backend.prompts.playwright_prompt import (
    build_playwright_prompt,
)


class PromptManager:
    """
    Central location for all AI prompts.
    """

    @staticmethod
    def testcase(
        repository_context: dict,
        file_name: str,
        chunk: str,
    ):

        return build_testcase_prompt(
            repository_context=repository_context,
            file_name=file_name,
            code=chunk,
        )

    @staticmethod
    def playwright(context: str):

        return build_playwright_prompt(context)