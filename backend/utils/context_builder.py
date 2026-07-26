class ContextBuilder:

    @staticmethod
    def build(routes):

        if not routes:

            return "No routes discovered."

        text = "Available API Endpoints:\n\n"

        for r in routes:

            text += f"{r['method']} {r['route']}\n"

        return text