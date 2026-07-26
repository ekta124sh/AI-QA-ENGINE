import re


class PlaywrightValidator:
    """
    Validates AI-generated Playwright Python code before saving it.
    """

    FORBIDDEN = [
        "sync_playwright(",
        "@pytest.fixture",
        "fixture(",
        "example.com",
        "api.example.com",
        "browser.launch(",
        "chromium.launch(",
        "firefox.launch(",
        "webkit.launch(",
        "time.sleep(",
        "while True",
        "exit(",
        "quit(",
        "input(",
    ]

    REQUIRED = [
        "def test_",
        "Page",
        "page.",
    ]

    @staticmethod
    def duplicate_tests(code: str) -> bool:
        """
        Returns True if duplicate test function names exist.
        """
        tests = re.findall(r"def\s+(test_\w+)", code)
        return len(tests) != len(set(tests))

    @staticmethod
    def long_urls(code: str):
        """
        Detect hallucinated URLs.
        """
        urls = re.findall(r"https?://\S+", code)

        errors = []

        for url in urls:

            if len(url) > 250:
                errors.append(
                    f"URL exceeds 250 characters: {url[:60]}..."
                )

        return errors

    @classmethod
    def validate(cls, code: str):

        errors = []

        # --------------------------
        # Empty output
        # --------------------------
        if not code or not code.strip():
            errors.append("Generated code is empty.")
            return errors

        # --------------------------
        # Forbidden patterns
        # --------------------------
        for item in cls.FORBIDDEN:

            if item in code:
                errors.append(f"Forbidden usage: {item}")

        # --------------------------
        # Required patterns
        # --------------------------
        for item in cls.REQUIRED:

            if item not in code:
                errors.append(f"Missing required pattern: {item}")

        # --------------------------
        # Imports
        # --------------------------
        if "from playwright.sync_api import" not in code:
            errors.append(
                "Missing Playwright import."
            )

        # --------------------------
        # Test functions
        # --------------------------
        tests = re.findall(r"def\s+(test_\w+)", code)

        if len(tests) == 0:
            errors.append(
                "No pytest test functions found."
            )

        # --------------------------
        # Duplicate test names
        # --------------------------
        if cls.duplicate_tests(code):
            errors.append(
                "Duplicate test function names found."
            )

        # --------------------------
        # Long URLs
        # --------------------------
        errors.extend(cls.long_urls(code))

        return errors