from collections import defaultdict


class ResultMerger:
    """
    Merges AI results from multiple tasks into a single dataset.
    """

    @staticmethod
    def merge(tasks):

        merged = []

        seen = set()

        for task in tasks:

            for testcase in task.get("testcases", []):

                key = (
                    testcase.get("title", "").strip().lower(),
                    testcase.get("module", "").strip().lower(),
                )

                if key in seen:
                    continue

                seen.add(key)

                testcase["workflow"] = task.get(
                    "workflow",
                    "General",
                )

                merged.append(testcase)

        merged = sorted(
            merged,
            key=lambda tc: (
                tc.get("workflow", ""),
                tc.get("module", ""),
                {
                    "Critical": 1,
                    "High": 2,
                    "Medium": 3,
                    "Low": 4,
                }.get(tc.get("priority"), 99),
            ),
        )

        return merged

    @staticmethod
    def summary(testcases):

        summary = defaultdict(int)

        for tc in testcases:

            summary["Total"] += 1

            summary[
                tc.get("priority", "Unknown")
            ] += 1

            summary[
                tc.get("type", "Unknown")
            ] += 1

        return dict(summary)