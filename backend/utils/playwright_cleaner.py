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

        # Replace placeholder URLs
        code = code.replace(
            "https://example.com",
            "http://127.0.0.1:8000/docs",
        )

        code = code.replace(
            "http://example.com",
            "http://127.0.0.1:8000/docs",
        )

        code = code.replace(
            "https://api.example.com",
            "http://127.0.0.1:8000/docs",
        )

        code = code.replace(
            "http://api.example.com",
            "http://127.0.0.1:8000/docs",
        )

        # Remove trailing whitespace
        code = "\n".join(
            line.rstrip() for line in code.splitlines()
        )

        # Remove extra blank lines
        code = re.sub(r"\n{3,}", "\n\n", code)

        return code.strip()