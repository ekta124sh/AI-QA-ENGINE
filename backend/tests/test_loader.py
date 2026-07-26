from backend.utils.code_loader import load_code

code = load_code(
    "repositories/fastapi/fastapi/applications.py"
)

print(code[:1000])