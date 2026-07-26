from pathlib import Path


SUPPORTED_EXTENSIONS = [
    ".py",
    ".java",
    ".js",
    ".ts",
    ".jsx",
    ".tsx",
    ".go",
    ".cpp",
    ".c",
    ".cs",
]


def scan_repository(repo_path: str):
    files = []

    for file in Path(repo_path).rglob("*"):
        if file.suffix.lower() in SUPPORTED_EXTENSIONS:
            files.append(str(file))

    return files