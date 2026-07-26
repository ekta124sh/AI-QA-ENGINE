def build_playwright_prompt(test_case: str) -> str:
    return f"""
You are a Senior QA Automation Engineer.

Generate ONLY executable Python Playwright code.

STRICT RULES:

1. Output ONLY Python code.
2. Do NOT return JSON.
3. Do NOT return a dictionary.
4. Do NOT return a list.
5. Do NOT wrap the code inside markdown.
6. Do NOT use triple backticks.
7. The first line must be:
import pytest
8. Use Playwright Sync API.
9. Create at least one pytest function beginning with:
def test_
10. Include meaningful assertions.
11. The code must run directly with:
pytest

Manual Test Case:

{test_case}
"""