import re


class TestCaseParser:

    @staticmethod
    def parse(response: str):

        """
        Splits Gemini output into individual test cases.
        """

        pattern = r"(?=\d+\.\s*\*\*Test Case ID)"

        parts = re.split(pattern, response)

        testcases = []

        for part in parts:

            part = part.strip()

            if not part:
                continue

            testcases.append(part)

        return testcases