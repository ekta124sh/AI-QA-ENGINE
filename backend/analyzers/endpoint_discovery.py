import ast
from pathlib import Path


class EndpointDiscovery:
    """
    Discovers FastAPI endpoints and extracts endpoint metadata.
    """

    HTTP_METHODS = {
        "get",
        "post",
        "put",
        "delete",
        "patch",
        "options",
        "head",
    }

    @staticmethod
    def _get_constant(node):

        if isinstance(node, ast.Constant):
            return node.value

        return None

    @staticmethod
    def _get_name(node):

        if isinstance(node, ast.Name):
            return node.id

        if isinstance(node, ast.Attribute):
            return node.attr

        return None

    @staticmethod
    def discover(repo_path: str):

        endpoints = []

        repo = Path(repo_path)

        for file in repo.rglob("*.py"):

            try:

                source = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

                tree = ast.parse(source)

            except Exception:
                continue

            for node in ast.walk(tree):

                if not isinstance(node, ast.FunctionDef):
                    continue

                for decorator in node.decorator_list:

                    if not isinstance(decorator, ast.Call):
                        continue

                    if not isinstance(decorator.func, ast.Attribute):
                        continue

                    method = decorator.func.attr.lower()

                    if method not in EndpointDiscovery.HTTP_METHODS:
                        continue

                    endpoint = {
                        "method": method.upper(),
                        "path": "",
                        "function": node.name,
                        "file": file.name,
                        "response_model": None,
                        "status_code": None,
                        "tags": [],
                        "summary": None,
                        "description": None,
                    }

                    # -------------------------
                    # Route
                    # -------------------------

                    if decorator.args:

                        first_arg = decorator.args[0]

                        if (
                            isinstance(first_arg, ast.Constant)
                            and isinstance(first_arg.value, str)
                        ):
                            endpoint["path"] = first_arg.value

                    # -------------------------
                    # Keyword Arguments
                    # -------------------------

                    for keyword in decorator.keywords:

                        key = keyword.arg
                        value = keyword.value

                        if key == "response_model":
                            endpoint["response_model"] = (
                                EndpointDiscovery._get_name(value)
                            )

                        elif key == "status_code":
                            endpoint["status_code"] = (
                                EndpointDiscovery._get_constant(value)
                            )

                        elif key == "summary":
                            endpoint["summary"] = (
                                EndpointDiscovery._get_constant(value)
                            )

                        elif key == "description":
                            endpoint["description"] = (
                                EndpointDiscovery._get_constant(value)
                            )

                        elif key == "tags":

                            if isinstance(value, ast.List):

                                endpoint["tags"] = [

                                    elt.value

                                    for elt in value.elts

                                    if isinstance(
                                        elt,
                                        ast.Constant,
                                    )
                                ]

                    endpoints.append(endpoint)

        return endpoints