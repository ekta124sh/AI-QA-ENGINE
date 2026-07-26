from pathlib import Path


class RepositoryAnalyzer:

    @staticmethod
    def analyze(repo_path: str):

        repo = Path(repo_path)

        analysis = {
            "repository_name": repo.name,
            "language": "Unknown",
            "framework": "Unknown",
            "database": "Unknown",
            "orm": "Unknown",
            "authentication": "Unknown",
            "testing": "Unknown",
            "containerization": "Unknown",

            "statistics": {
                "python_files": 0,
                "javascript_files": 0,
                "typescript_files": 0,
                "java_files": 0,
                "go_files": 0,
                "total_source_files": 0,
            }
        }

        source_files = []

        for file in repo.rglob("*"):

            if not file.is_file():
                continue

            suffix = file.suffix.lower()

            if suffix == ".py":
                analysis["statistics"]["python_files"] += 1
                source_files.append(file)

            elif suffix == ".js":
                analysis["statistics"]["javascript_files"] += 1
                source_files.append(file)

            elif suffix == ".ts":
                analysis["statistics"]["typescript_files"] += 1
                source_files.append(file)

            elif suffix == ".java":
                analysis["statistics"]["java_files"] += 1
                source_files.append(file)

            elif suffix == ".go":
                analysis["statistics"]["go_files"] += 1
                source_files.append(file)

        analysis["statistics"]["total_source_files"] = len(source_files)

        # -----------------------------
        # Detect Primary Language
        # -----------------------------

        stats = analysis["statistics"]

        language_map = {
            "python_files": "Python",
            "javascript_files": "JavaScript",
            "typescript_files": "TypeScript",
            "java_files": "Java",
            "go_files": "Go",
        }

        max_count = 0

        for key, language in language_map.items():

            if stats[key] > max_count:
                max_count = stats[key]
                analysis["language"] = language

        # -----------------------------
        # Scan important files
        # -----------------------------

        files_to_scan = []

        for name in [
            "requirements.txt",
            "pyproject.toml",
            "package.json",
            "Dockerfile",
        ]:
            files_to_scan.extend(repo.rglob(name))

        for file in files_to_scan:

            try:

                content = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                ).lower()

                if "fastapi" in content:
                    analysis["framework"] = "FastAPI"

                elif "flask" in content:
                    analysis["framework"] = "Flask"

                elif "django" in content:
                    analysis["framework"] = "Django"

                elif "express" in content:
                    analysis["framework"] = "Express"

                if "sqlalchemy" in content:
                    analysis["orm"] = "SQLAlchemy"

                if (
                    "psycopg2" in content
                    or "postgresql" in content
                    or "asyncpg" in content
                ):
                    analysis["database"] = "PostgreSQL"

                if "mysql" in content:
                    analysis["database"] = "MySQL"

                if "sqlite" in content:
                    analysis["database"] = "SQLite"

                if (
                    "python-jose" in content
                    or "jwt" in content
                    or "pyjwt" in content
                ):
                    analysis["authentication"] = "JWT"

                if "pytest" in content:
                    analysis["testing"] = "Pytest"

                if file.name == "Dockerfile":
                    analysis["containerization"] = "Docker"

            except Exception:
                pass

        return analysis