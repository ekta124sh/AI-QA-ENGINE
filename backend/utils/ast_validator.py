import ast


class ASTValidator:

    @staticmethod
    def validate(code: str):

        try:

            ast.parse(code)

            return True, None

        except SyntaxError as e:

            return False, str(e)