from backend.utils.code_loader import load_code
from backend.utils.code_chunker import chunk_code

code = load_code(
    "repositories/fastapi/fastapi/applications.py"
)

chunks = chunk_code(code)

print(f"Total Chunks: {len(chunks)}")

print("=" * 80)

print(chunks[0])

print("=" * 80)

print(chunks[1])