# allow to use navigation keys in input()
import readline

from binary_set import BinarySet
from expression import Expression, ExpressionParseError, ExpressionEvalError

expr = ""

while True:
    inp = input("Type expression: ")

    try:
        expr = Expression(inp)

        if len(expr.variables) < 1:
            print("Parse error: Expression must have at least one variable")
            continue

        try:
            row_set = (0 for x in range(len(expr.variables)))
            expr.calc(row_set)
        except ExpressionEvalError as e:
            print("Eval error:", e)
            continue
    except ExpressionParseError as e:
        print("Parse error:", e)
        continue

    print("Postfix notation:", expr.expr)

    # print header of truth table
    SPAN_BEFORE_F = "  "
    print("\n" + " ".join(expr.variables) + SPAN_BEFORE_F + "F")

    row_set = BinarySet(len(expr.variables))
    while True:
        f = expr.calc(tuple(row_set))
        print(str(row_set) + SPAN_BEFORE_F + str(f))

        if not row_set.next():
            break

    print()
