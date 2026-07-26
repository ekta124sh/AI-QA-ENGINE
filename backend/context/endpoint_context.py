from copy import deepcopy


class EndpointContext:
    """
    Creates a repository context focused on a single endpoint.
    """

    @staticmethod
    def build(repository_context: dict, endpoint: dict) -> dict:

        context = deepcopy(repository_context)

        context["current_endpoint"] = endpoint
        context["endpoints"] = [endpoint]

        return context