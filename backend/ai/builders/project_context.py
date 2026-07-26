class ProjectContext:

    @staticmethod
    def build(info):

        text = ""

        text += f"Framework: {info.get('framework')}\n"
        text += f"Database: {info.get('database')}\n"
        text += f"ORM: {info.get('orm')}\n\n"

        text += "Models:\n"

        for model in sorted(set(info["models"])):
            text += f" - {model}\n"

        text += "\nRouters:\n"

        for router in sorted(set(info["routers"])):
            text += f" - {router}\n"

        text += "\nAuthentication:\n"

        if info["authentication"]:
            for auth in sorted(set(info["authentication"])):
                text += f" - {auth}\n"
        else:
            text += " - None\n"

        return text