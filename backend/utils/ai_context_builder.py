class AIContextBuilder:

    @staticmethod
    def build(
        project_context: str,
        repository_context: str,
        manual_test_case: str,
    ):

        return f"""
You are generating Playwright automation for ONE manual test case.

====================================================
PROJECT INFORMATION
====================================================

{project_context}

====================================================
APPLICATION ROUTES
====================================================

{repository_context}

====================================================
CURRENT MANUAL TEST CASE
====================================================

{manual_test_case}
"""