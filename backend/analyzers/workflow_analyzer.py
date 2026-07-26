from collections import defaultdict


class WorkflowAnalyzer:
    """
    Groups related endpoints into business workflows.
    """

    @staticmethod
    def analyze(endpoints):

        workflows = []

        grouped = defaultdict(list)

        # ----------------------------------------------------
        # Group endpoints by first path segment
        # ----------------------------------------------------

        for endpoint in endpoints:

            path = endpoint.get("path", "/")

            parts = [
                part
                for part in path.split("/")
                if part
            ]

            if not parts:
                group = "General"
            else:
                group = parts[0].title()

            grouped[group].append(endpoint)

        # ----------------------------------------------------
        # Build workflow
        # ----------------------------------------------------

        order = {
            "POST": 1,
            "GET": 2,
            "PUT": 3,
            "PATCH": 4,
            "DELETE": 5,
        }

        for workflow_name, items in grouped.items():

            items = sorted(
                items,
                key=lambda x: (
                    order.get(
                        x.get("method", "").upper(),
                        99
                    ),
                    x.get("path", ""),
                ),
            )

            workflow = {
                "name": workflow_name,
                "steps": [],
            }

            for endpoint in items:

                workflow["steps"].append(
                    {
                        "method": endpoint.get("method"),
                        "path": endpoint.get("path"),
                        "function": endpoint.get("function"),
                        "request_model": endpoint.get("request_model"),
                        "response_model": endpoint.get("response_model"),
                    }
                )

            workflows.append(workflow)

        return workflows