import os
import re


class RepositoryAnalyzer:
    """
    Scans a cloned repository and extracts FastAPI routes.
    """

    @staticmethod
    def find_routes(repo_path: str):

        routes = []

        for root, _, files in os.walk(repo_path):

            for file in files:

                if not file.endswith(".py"):
                    continue

                full_path = os.path.join(root, file)

                try:

                    with open(full_path, "r", encoding="utf-8") as f:
                        code = f.read()

                except Exception:
                    continue

                matches = re.findall(
                    r'@(router|app)\.(get|post|put|delete|patch)\("([^"]+)"',
                    code,
                )

                for _, method, route in matches:

                    routes.append(
                        {
                            "method": method.upper(),
                            "route": route,
                            "file": file,
                        }
                    )

        return routes