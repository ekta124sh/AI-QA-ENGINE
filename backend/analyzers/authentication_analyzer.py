import ast
from pathlib import Path


class AuthenticationAnalyzer:
    """
    Discovers authentication mechanisms used by the project.
    """

    @staticmethod
    def analyze(repo_path: str):

        repo = Path(repo_path)

        analysis = {
            "type": "Unknown",
            "oauth2": False,
            "jwt": False,
            "api_key": False,
            "basic_auth": False,
            "protected_endpoints": [],
            "dependencies": [],
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

            content = source.lower()

            # ------------------------------------------
            # Authentication Detection
            # ------------------------------------------

            if "oauth2passwordbearer" in content:
                analysis["oauth2"] = True
                analysis["type"] = "OAuth2"

            if "jwt" in content or "pyjwt" in content:
                analysis["jwt"] = True

            if "apikey" in content:
                analysis["api_key"] = True

            if "basicauth" in content:
                analysis["basic_auth"] = True

            # ------------------------------------------
            # Depends(...)
            # ------------------------------------------

            for node in ast.walk(tree):

                if not isinstance(node, ast.Call):
                    continue

                if isinstance(node.func, ast.Name):

                    if node.func.id == "Depends":

                        if node.args:

                            dependency = ast.unparse(node.args[0])

                            analysis["dependencies"].append(
                                dependency
                            )

            # ------------------------------------------
            # Protected Endpoints
            # ------------------------------------------

            for node in ast.walk(tree):

                if not isinstance(node, ast.FunctionDef):
                    continue

                decorators = []

                for dec in node.decorator_list:

                    if (
                        isinstance(dec, ast.Call)
                        and isinstance(dec.func, ast.Attribute)
                    ):

                        decorators.append(dec.func.attr)

                http_methods = {
                    "get",
                    "post",
                    "put",
                    "delete",
                    "patch",
                }

                if not any(
                    method in decorators
                    for method in http_methods
                ):
                    continue

                has_depends = False

                for arg in node.args.args:

                    if arg.annotation:

                        if "Depends" in ast.unparse(arg.annotation):
                            has_depends = True

                if has_depends:

                    analysis["protected_endpoints"].append(
                        {
                            "function": node.name,
                            "file": file.name,
                        }
                    )

        return analysis