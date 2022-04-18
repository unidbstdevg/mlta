import operators


class Expression:
    expr = ""

    # construct prefix notation
    def __init__(self, string):
        # hack to interprete parenthesis as separate word
        string = string.replace("(", " ( ")
        string = string.replace(")", " ) ")

        stack = []

        words = string.split(" ")
        for w in words:
            if w == "":
                continue

            if w == ")":
                while len(stack) != 0:
                    tc = stack.pop()
                    if tc == "(":
                        break

                    self.expr += tc + " "

                if len(stack) == 0:
                    raise ExpressionParseError("Missed opening parenthesis")
            else:
                if operators.is_operator(w) or w == "(":
                    stack.append(w)
                else:
                    # TODO; variables should be one letter
                    self.expr += w + " "

        while len(stack) != 0:
            tc = stack.pop()
            if tc == "(":
                raise ExpressionParseError("Missed closing parenthesis")

            self.expr += tc + " "


class ExpressionParseError(Exception):
    pass
