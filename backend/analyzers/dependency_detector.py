from pathlib import Path


class DependencyDetector:

    DEPENDENCIES = {
        "database": {
            "PostgreSQL": ["psycopg2", "asyncpg", "postgresql"],
            "MySQL": ["mysqlclient", "pymysql", "mysql"],
            "SQLite": ["sqlite3"],
            "MongoDB": ["pymongo", "motor", "mongodb"],
        },

        "orm": {
            "SQLAlchemy": ["sqlalchemy"],
            "Django ORM": ["django.db.models"],
            "Prisma": ["prisma"],
            "Hibernate": ["hibernate"],
        },

        "authentication": {
            "JWT": ["jwt", "pyjwt", "python-jose"],
            "OAuth2": ["oauth2", "OAuth2PasswordBearer"],
        },

        "testing": {
            "Pytest": ["pytest"],
            "JUnit": ["junit"],
            "Jest": ["jest"],
        },

        "containerization": {
            "Docker": ["docker"],
        }
    }

    @staticmethod
    def detect(repo_path: str):

        detected = {
            "database": "Unknown",
            "orm": "Unknown",
            "authentication": "Unknown",
            "testing": "Unknown",
            "containerization": "Unknown",
        }

        repo = Path(repo_path)

        files_to_scan = []

        for name in [
            "requirements.txt",
            "pyproject.toml",
            "package.json",
            "pom.xml",
            "build.gradle",
            "go.mod",
            "Dockerfile",
        ]:

            files_to_scan.extend(repo.rglob(name))

        for file in files_to_scan:

            try:

                content = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                ).lower()

                for category, values in DependencyDetector.DEPENDENCIES.items():

                    if detected[category] != "Unknown":
                        continue

                    for tech, keywords in values.items():

                        for keyword in keywords:

                            if keyword.lower() in content:
                                detected[category] = tech
                                break

                        if detected[category] != "Unknown":
                            break

            except Exception:
                continue

        return detected