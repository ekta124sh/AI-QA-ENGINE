from backend.utils.code_loader import load_code
from backend.agents.testcase_agent import TestCaseAgent

code = load_code(
    "repositories/fastapi/fastapi/applications.py"
)

agent = TestCaseAgent()

answer = agent.generate(code)

print(answer)