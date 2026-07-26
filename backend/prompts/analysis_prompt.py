def build_analysis_prompt(
    test_case: str,
    playwright_code: str,
    error_log: str,
):

    return f"""
You are a Senior QA Automation Architect.

Analyze why this Playwright test failed.

==========================
MANUAL TEST CASE
==========================

{test_case}

==========================
PLAYWRIGHT SCRIPT
==========================

{playwright_code}

==========================
ERROR
==========================

{error_log}

==========================
Return:

1. Root Cause

2. Why it failed

3. How to fix it

4. Improved Playwright code (if necessary)

Keep the answer concise.
"""