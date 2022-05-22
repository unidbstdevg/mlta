import operators

CONSTANTS = ("0", "1")


class Expression:

    # construct prefix notation
    def __init__(self, string):
        self.expr = ""
        self.variables = set()

        # hack to interpret parenthesis as separate word
        string = string.replace("(", " ( ")
        string = string.replace(")", " ) ")
        # hack to interpret '!' as separate word
        string = string.replace("!", " ! ")

        stack = []

        words = string.split(" ")
        for w in words:
            if w == "":
                continue

            if w in CONSTANTS:
                self.expr += w + " "
                continue

            if operators.is_operator(w) and operators.operands_count(w) == 1:
                stack.append(w)
                continue

            if w == "(":
                stack.append(w)
                continue

            if w == ")":
                while len(stack) != 0:
                    tc = stack.pop()
                    if tc == "(":
                        break

                    self.expr += tc + " "
                continue

            if operators.is_operator(w):
                priority = operators.get_operator_priority(w)
                while len(stack) != 0:
                    t = stack.pop()
                    if t != "(":
                        t_priority = \
                            operators.get_operator_priority(t)
                        if t_priority >= priority:
                            self.expr += t + " "
                            continue

                    stack.append(t)
                    break

                stack.append(w)
                continue

            if w.isupper() or not w.isalpha():
                raise ExpressionParseError(
                    "Not an operator: \"{}\". Type 'help' (or '?') for list of operators"
                    .format(w))

            if len(w) > 1:
                raise ExpressionParseError(
                    "Variables should be one letter: \"{}\"".format(w))
            if not w.islower:
                raise ExpressionParseError(
                    "Variables should be in lower case: \"{}\"".format(w))

            self.expr += w + " "
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
            elif w == "":
                print("Unreachable reached: w == \"\"")
                exit(1)
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

        if len(operands) > 1:
            raise ExpressionEvalError("Are you missed operator?")

        if len(operands) == 0:
            print("Unreachable reached: operands.empty()")
            exit(1)

        f = operands.pop()
        return f


class ExpressionParseError(Exception):
    pass


class ExpressionEvalError(Exception):
    pass
