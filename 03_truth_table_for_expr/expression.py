import operators

CONSTANTS = ("0", "1")


class Expression:
    expr = ""
    variables = set()

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
                elif w.isupper() or (not w.isalpha() and w not in CONSTANTS):
                    raise ExpressionParseError(
                        "Not an operator: \"{}\". Should be one of delcared in operators.py"
                        .format(w))
                else:
                    if len(w) > 1:
                        raise ExpressionParseError(
                            "Variables should be one letter: \"{}\"".format(w))
                    if not w.islower:
                        raise ExpressionParseError(
                            "Variables should be in lower case: \"{}\"".format(
                                w))

                    self.expr += w + " "
                    if w not in CONSTANTS:
                        self.variables.add(w)

        while len(stack) != 0:
            tc = stack.pop()
            if tc == "(":
                raise ExpressionParseError("Missed closing parenthesis")

            self.expr += tc + " "

        # remove trailing space
        self.expr = self.expr[:-1]

        self.variables = sorted(self.variables)

    def _substitute_operands(self, row_set):
        res = self.expr

        for var, val in zip(self.variables, row_set):
            res = res.replace(var, str(val))

        return res

    def calc(self, row_set):
        final_expr = self._substitute_operands(row_set)

        operands = []

        words = final_expr.split(" ")
        for w in words:
            if w in CONSTANTS:
                operands.append(w)
            else:
                operator = w

                cur_operands = []
                operands_count = operators.operands_count(operator)
                for _ in range(operands_count):
                    if len(operands) == 0:
                        raise ExpressionEvalError(
                            "Wrong operands count for operator " + operator)

                    new_operand = operands.pop()
                    cur_operands.append(new_operand)

                f = str(operators.apply_operator(operator, cur_operands))

                operands.append(f)

        f = operands.pop()
        return f


class ExpressionParseError(Exception):
    pass


class ExpressionEvalError(Exception):
    pass
