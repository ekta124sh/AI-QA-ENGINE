import ast
from pathlib import Path


class ModelAnalyzer:
    """
    Discovers Pydantic BaseModel classes and extracts
    field information for AI prompt generation.
    """

    @staticmethod
    def analyze(repo_path: str):

        repo = Path(repo_path)

        models = {}

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

                if not isinstance(node, ast.ClassDef):
                    continue

                # Check if class inherits from BaseModel
                is_model = False

                for base in node.bases:

                    if isinstance(base, ast.Name):
                        if base.id == "BaseModel":
                            is_model = True

                    elif isinstance(base, ast.Attribute):
                        if base.attr == "BaseModel":
                            is_model = True

                if not is_model:
                    continue

                fields = []

                for item in node.body:

                    if not isinstance(item, ast.AnnAssign):
                        continue

                    field_name = (
                        item.target.id
                        if isinstance(item.target, ast.Name)
                        else None
                    )

                    field_type = None

                    if isinstance(item.annotation, ast.Name):
                        field_type = item.annotation.id

                    elif isinstance(item.annotation, ast.Attribute):
                        field_type = item.annotation.attr

                    elif isinstance(item.annotation, ast.Subscript):

                        if isinstance(item.annotation.value, ast.Name):
                            field_type = item.annotation.value.id

                    fields.append(
                        {
                            "name": field_name,
                            "type": field_type,
                            "required": item.value is None,
                        }
                    )

                models[node.name] = {
                    "file": file.name,
                    "fields": fields,
                }

        return models