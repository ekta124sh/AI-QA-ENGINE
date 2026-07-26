from typing import List, Dict


class AnalysisPlanner:
    """
    Creates AI tasks from repository analysis.

    Each endpoint becomes one AI task.
    """

    @staticmethod
    def create_tasks(repository_context: dict) -> List[Dict]:

        tasks = []

        endpoints = repository_context.get(
            "endpoints",
            []
        )

        workflows = repository_context.get(
            "workflow_analysis",
            []
        )

        workflow_lookup = {}

        for workflow in workflows:

            workflow_name = workflow["name"]

            for step in workflow["steps"]:

                key = (
                    step["method"],
                    step["path"]
                )

                workflow_lookup[key] = workflow_name

        for endpoint in endpoints:

            key = (
                endpoint.get("method"),
                endpoint.get("path")
            )

            task = {

                "task_id": len(tasks) + 1,

                "type": "endpoint",

                "workflow": workflow_lookup.get(
                    key,
                    "General"
                ),

                "method": endpoint.get("method"),

                "path": endpoint.get("path"),

                "function": endpoint.get("function"),

                "request_model": endpoint.get(
                    "request_model"
                ),

                "response_model": endpoint.get(
                    "response_model"
                ),

                "status": "Pending"
            }

            tasks.append(task)

        return tasks