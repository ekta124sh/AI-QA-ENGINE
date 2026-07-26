from pathlib import Path


def load_code(file_path: str):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        return file.read()