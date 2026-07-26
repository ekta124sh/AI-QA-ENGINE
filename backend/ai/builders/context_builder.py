class ContextBuilder:

    @staticmethod
    def build(routes):

        if not routes:
            return "No API routes discovered."

        text = "Available API Endpoints:\n\n"

        for route in routes:
            text += f"{route['method']} {route['route']}\n"

        return text