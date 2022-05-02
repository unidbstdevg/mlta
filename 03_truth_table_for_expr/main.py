# allow to use navigation keys in input()
import readline

from binary_set import BinarySet
from expression import Expression, ExpressionParseError

expr = ""

while True:
    inp = input("Type expression: ")
    try:
        expr = Expression(inp)
        print("Postfix notation:", expr.expr)
        break
    except ExpressionParseError as e:
        print("Parse error:", e)
        continue

# print header of truth table
SPAN_BEFORE_F = "  "
print("\n" + " ".join(expr.variables) + SPAN_BEFORE_F + "f")

row_set = BinarySet(len(expr.variables))
while True:
    f = expr.calc(tuple(row_set))
    print(str(row_set) + SPAN_BEFORE_F + str(f))

    if not row_set.next():
        break

input()
