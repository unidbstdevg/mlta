import operators


class Expression:
    expr = ""
    variables = []

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
                elif w.isupper():
                    raise ExpressionParseError(
                        "Not an operator: \"{}\"".format(w))
                else:
                    if len(w) > 1:
                        raise ExpressionParseError(
                            "Variables should be one letter: \"{}\"".format(w))
                    if not w.islower:
                        raise ExpressionParseError(
                            "Variables should be in lower case: \"{}\"".format(
                                w))

                    self.expr += w + " "
                    self.variables.append(w)

        while len(stack) != 0:
            tc = stack.pop()
            if tc == "(":
                raise ExpressionParseError("Missed closing parenthesis")

            self.expr += tc + " "

        # remove trailing space
        self.expr = self.expr[:-1]


class ExpressionParseError(Exception):
    pass
