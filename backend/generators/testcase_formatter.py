import json
from typing import Any, Dict, List


class TestCaseFormatter:
    """
    Formats, validates and normalizes AI generated test cases.
    """

    REQUIRED_FIELDS = [
        "title",
        "module",
        "priority",
        "severity",
        "test_type",
        "preconditions",
        "steps",
        "expected_result",
    ]

    PRIORITY_ORDER = {
        "Critical": 1,
        "High": 2,
        "Medium": 3,
        "Low": 4,
    }

    DEFAULT_VALUES = {
        "title": "",
        "module": "General",
        "priority": "Medium",
        "severity": "Medium",
        "test_type": "Functional",
        "preconditions": "",
        "steps": [],
        "expected_result": "",
    }

    @staticmethod
    def format(llm_response: str) -> List[Dict[str, Any]]:

        parsed = TestCaseFormatter._parse_json(llm_response)

        parsed = TestCaseFormatter._normalize(parsed)

        parsed = TestCaseFormatter._remove_duplicates(parsed)

        parsed = TestCaseFormatter._assign_ids(parsed)

        parsed = TestCaseFormatter._sort(parsed)

        return parsed

    @staticmethod
    def _clean_response(response: str) -> str:

        if response is None:
            raise Exception("LLM returned an empty response.")

        response = response.strip()

        if response.startswith("```json"):
            response = response[7:]

        if response.startswith("```"):
            response = response[3:]

        if response.endswith("```"):
            response = response[:-3]

        return response.strip()

    @staticmethod
    def _parse_json(response: str):

        response = TestCaseFormatter._clean_response(response)

        try:

            parsed = json.loads(response)

        except json.JSONDecodeError as ex:

            print("\n" + "=" * 80)
            print("INVALID JSON RECEIVED FROM LLM")
            print("=" * 80)
            print(response)
            print("=" * 80)

            raise Exception(
                f"LLM returned invalid JSON.\n\n{ex}"
            )

        if isinstance(parsed, dict):
            parsed = [parsed]

        if not isinstance(parsed, list):
            raise Exception(
                "LLM output must be a JSON array."
            )

        return parsed

    @staticmethod
    def _normalize(testcases):

        normalized = []

        for tc in testcases:

            new_tc = {}

            for field in TestCaseFormatter.REQUIRED_FIELDS:

                new_tc[field] = tc.get(
                    field,
                    TestCaseFormatter.DEFAULT_VALUES[field],
                )

            if (
                not new_tc["test_type"]
                and "type" in tc
            ):
                new_tc["test_type"] = tc["type"]

            if not isinstance(new_tc["steps"], list):

                new_tc["steps"] = [
                    str(new_tc["steps"])
                ]

            priority = str(
                new_tc["priority"]
            ).capitalize()

            if priority not in TestCaseFormatter.PRIORITY_ORDER:
                priority = "Medium"

            new_tc["priority"] = priority

            normalized.append(new_tc)

        return normalized

    @staticmethod
    def _remove_duplicates(testcases):

        unique = []
        seen = set()

        for tc in testcases:

            key = (
                tc["title"].strip().lower(),
                tc["module"].strip().lower(),
            )

            if key in seen:
                continue

            seen.add(key)

            unique.append(tc)

        return unique

    @staticmethod
    def _assign_ids(testcases):

        for index, tc in enumerate(
            testcases,
            start=1,
        ):

            tc["id"] = f"TC_{index:04d}"

        return testcases

    @staticmethod
    def _sort(testcases):

        return sorted(
            testcases,
            key=lambda tc: (
                TestCaseFormatter.PRIORITY_ORDER.get(
                    tc["priority"],
                    99,
                ),
                tc["title"],
            ),
        )