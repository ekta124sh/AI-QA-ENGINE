import ast
from pathlib import Path


class DatabaseAnalyzer:
    """
    Discovers SQLAlchemy models and CRUD operations.
    """

    @staticmethod
    def analyze(repo_path: str):

        repo = Path(repo_path)

        analysis = {
            "models": [],
            "crud_operations": [],
            "tables": []
        }

        crud_methods = {
            "add": "CREATE",
            "commit": "COMMIT",
            "delete": "DELETE",
            "query": "READ",
            "execute": "EXECUTE",
            "update": "UPDATE",
            "merge": "MERGE",
            "refresh": "REFRESH",
        }

        for file in repo.rglob("*.py"):

            try:

                source = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

                tree = ast.parse(source)

            except Exception:
                continue

            # ----------------------------------------
            # SQLAlchemy Models
            # ----------------------------------------

            for node in ast.walk(tree):

                if isinstance(node, ast.ClassDef):

                    for base in node.bases:

                        if isinstance(base, ast.Name):

                            if base.id == "Base":

                                analysis["models"].append(
                                    {
                                        "model": node.name,
                                        "file": file.name,
                                    }
                                )

            # ----------------------------------------
            # CRUD Detection
            # ----------------------------------------

            for node in ast.walk(tree):

                if not isinstance(node, ast.Call):
                    continue

                if not isinstance(node.func, ast.Attribute):
                    continue

                method = node.func.attr

                if method in crud_methods:

                    analysis["crud_operations"].append(
                        {
                            "operation": crud_methods[method],
                            "method": method,
                            "file": file.name,
                            "line": getattr(node, "lineno", None),
                        }
                    )

        analysis["tables"] = [
            model["model"]
            for model in analysis["models"]
        ]

        return analysis