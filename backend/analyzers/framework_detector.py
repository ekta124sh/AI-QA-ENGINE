from pathlib import Path


class FrameworkDetector:

    FRAMEWORK_PATTERNS = {
        "FastAPI": [
            "from fastapi import",
            "FastAPI(",
        ],
        "Flask": [
            "from flask import",
            "Flask(",
        ],
        "Django": [
            "django",
            "manage.py",
        ],
        "Express": [
            "express(",
            "require('express')",
            'require("express")',
        ],
        "Spring Boot": [
            "@SpringBootApplication",
            "org.springframework.boot",
        ],
    }

    @staticmethod
    def detect(repo_path: str) -> str:
        """
        Detects the primary framework used in a repository.
        """

        repo = Path(repo_path)

        for file in repo.rglob("*"):

            if file.suffix.lower() not in [
                ".py",
                ".js",
                ".ts",
                ".java",
            ]:
                continue

            try:

                content = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

                for framework, patterns in FrameworkDetector.FRAMEWORK_PATTERNS.items():

                    for pattern in patterns:

                        if pattern in content:
                            return framework

            except Exception:
                continue

        return "Unknown"