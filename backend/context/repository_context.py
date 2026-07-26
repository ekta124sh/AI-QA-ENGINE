from pathlib import Path


class RepositoryContext:

    @staticmethod
    def build(
        analysis: dict,
        current_file: str,
    ):

        file_name = Path(current_file).name

        endpoints = [
            endpoint
            for endpoint in analysis.get("endpoints", [])
            if endpoint["file"] == file_name
        ]

        models = analysis.get("models", {})

        endpoint_models = {}

        for endpoint in endpoints:

            request_model = endpoint.get("request_model")
            response_model = endpoint.get("response_model")

            if request_model and request_model in models:
                endpoint_models[request_model] = models[request_model]

            if response_model and response_model in models:
                endpoint_models[response_model] = models[response_model]

        return {

            # Repository
            "repository_name": analysis.get("repository_name"),
            "language": analysis.get("language"),
            "framework": analysis.get("framework"),
            "database": analysis.get("database"),
            "orm": analysis.get("orm"),
            "authentication": analysis.get("authentication"),
            "testing": analysis.get("testing"),
            "containerization": analysis.get("containerization"),

            # Current File
            "current_file": file_name,

            # Endpoints
            "endpoints": endpoints,

            # Current Endpoint Models
            "models": endpoint_models,

            # Database Intelligence
            "database_analysis": analysis.get(
                "database_analysis",
                {}
            ),

            # Authentication Intelligence
            "authentication_analysis": analysis.get(
                "authentication_analysis",
                {}
            ),

            # Workflow Intelligence
            "workflow_analysis": analysis.get(
                "workflow_analysis",
                []
            ),
        }