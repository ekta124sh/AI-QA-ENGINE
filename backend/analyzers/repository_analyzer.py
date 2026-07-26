from pathlib import Path

from backend.analyzers.endpoint_discovery import EndpointDiscovery
from backend.analyzers.workflow_analyzer import WorkflowAnalyzer
from backend.analyzers.model_analyzer import ModelAnalyzer
from backend.analyzers.database_analyzer import DatabaseAnalyzer
from backend.analyzers.authentication_analyzer import AuthenticationAnalyzer


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
            },

            # Analysis Results
            "endpoints": [],
            "workflow_analysis": [],
            "models": {},
            "database_analysis": {},
            "authentication_analysis": {},
        }

        source_files = []

        # ---------------------------------------------------
        # Scan Source Files
        # ---------------------------------------------------

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

        # ---------------------------------------------------
        # Detect Primary Language
        # ---------------------------------------------------

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

        # ---------------------------------------------------
        # Detect Framework / Database / ORM
        # ---------------------------------------------------

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
                    "postgresql" in content
                    or "asyncpg" in content
                    or "psycopg2" in content
                ):
                    analysis["database"] = "PostgreSQL"

                elif "mysql" in content:
                    analysis["database"] = "MySQL"

                elif "sqlite" in content:
                    analysis["database"] = "SQLite"

                if (
                    "jwt" in content
                    or "python-jose" in content
                    or "pyjwt" in content
                ):
                    analysis["authentication"] = "JWT"

                elif "oauth2" in content:
                    analysis["authentication"] = "OAuth2"

                if "pytest" in content:
                    analysis["testing"] = "Pytest"

                if file.name == "Dockerfile":
                    analysis["containerization"] = "Docker"

            except Exception:
                pass

        # ---------------------------------------------------
        # Endpoint Discovery
        # ---------------------------------------------------

        print("\nDiscovering API Endpoints...")

        endpoints = EndpointDiscovery.discover(repo_path)

        analysis["endpoints"] = endpoints

        print(f"Endpoints Found : {len(endpoints)}")

        # ---------------------------------------------------
        # Workflow Analysis
        # ---------------------------------------------------

        print("\nAnalyzing Workflows...")

        workflow_analysis = WorkflowAnalyzer.analyze(endpoints)

        analysis["workflow_analysis"] = workflow_analysis

        print(
            f"Workflows Found : {len(workflow_analysis)}"
        )

        # ---------------------------------------------------
        # Model Discovery
        # ---------------------------------------------------

        print("\nDiscovering Models...")

        models = ModelAnalyzer.analyze(repo_path)

        analysis["models"] = models

        print(f"Models Found : {len(models)}")

        # ---------------------------------------------------
        # Database Analysis
        # ---------------------------------------------------

        print("\nAnalyzing Database...")

        database_analysis = DatabaseAnalyzer.analyze(repo_path)

        analysis["database_analysis"] = database_analysis

        print(
            f"Database Models : {len(database_analysis['models'])}"
        )

        print(
            f"CRUD Operations : {len(database_analysis['crud_operations'])}"
        )

        # ---------------------------------------------------
        # Authentication Analysis
        # ---------------------------------------------------

        print("\nAnalyzing Authentication...")

        authentication_analysis = AuthenticationAnalyzer.analyze(
            repo_path
        )

        analysis["authentication_analysis"] = authentication_analysis

        print(
            f"Authentication Type : {authentication_analysis['type']}"
        )

        print(
            f"Protected Endpoints : "
            f"{len(authentication_analysis['protected_endpoints'])}"
        )

        print("\nRepository Analysis Completed.")

        return analysis