import re


class PlaywrightCleaner:

    @staticmethod
    def clean(code: str) -> str:
        """
        Cleans LLM generated Playwright code.
        """

        if not code:
            return ""

        # Remove markdown fences
        code = code.replace("```python", "")
        code = code.replace("```", "")

        # Normalize line endings
        code = code.replace("\r\n", "\n")

        # Remove trailing whitespace
        code = "\n".join(line.rstrip() for line in code.splitlines())

        # Remove extra blank lines
        code = re.sub(r"\n{3,}", "\n\n", code)

        return code.strip()