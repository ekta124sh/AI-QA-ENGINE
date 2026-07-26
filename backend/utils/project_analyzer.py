import os
import re


class ProjectAnalyzer:
    """
    Analyze a cloned repository and collect useful project metadata.
    """

    @staticmethod
    def analyze(repo_path: str):

        info = {
            "framework": None,
            "database": None,
            "orm": None,
            "models": [],
            "routers": [],
            "middlewares": [],
            "authentication": [],
        }

        for root, _, files in os.walk(repo_path):

            for file in files:

                if not file.endswith(".py"):
                    continue

                path = os.path.join(root, file)

                try:
                    with open(path, "r", encoding="utf-8") as f:
                        code = f.read()

                except Exception:
                    continue

                # ----------------------------
                # Framework Detection
                # ----------------------------

                if "FastAPI(" in code:
                    info["framework"] = "FastAPI"

                elif "Flask(" in code:
                    info["framework"] = "Flask"

                elif "django" in code.lower():
                    info["framework"] = "Django"

                # ----------------------------
                # ORM Detection
                # ----------------------------

                if "sqlalchemy" in code.lower():
                    info["orm"] = "SQLAlchemy"

                # ----------------------------
                # Database Detection
                # ----------------------------

                if "postgresql://" in code.lower():
                    info["database"] = "PostgreSQL"

                elif "mysql://" in code.lower():
                    info["database"] = "MySQL"

                elif "sqlite" in code.lower():
                    info["database"] = "SQLite"

                # ----------------------------
                # SQLAlchemy Models
                # ----------------------------

                matches = re.findall(
                    r"class\s+(\w+)\(.*Base.*\)",
                    code,
                )

                info["models"].extend(matches)

                # ----------------------------
                # Routers
                # ----------------------------

                routers = re.findall(
                    r'APIRouter\(',
                    code,
                )

                if routers:
                    info["routers"].append(file)

                # ----------------------------
                # Middleware
                # ----------------------------

                middleware = re.findall(
                    r"add_middleware",
                    code,
                )

                if middleware:
                    info["middlewares"].append(file)

                # ----------------------------
                # Authentication
                # ----------------------------

                if "OAuth2" in code:
                    info["authentication"].append("OAuth2")

                if "JWT" in code.upper():
                    info["authentication"].append("JWT")

        return info