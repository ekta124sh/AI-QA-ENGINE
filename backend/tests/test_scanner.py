from backend.utils.file_scanner import scan_repository

files = scan_repository("repositories/fastapi")

print(f"Total Files: {len(files)}")

for file in files[:20]:
    print(file)