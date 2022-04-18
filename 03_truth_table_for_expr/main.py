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
print(" ".join(expr.variables) + SPAN_BEFORE_F + "f")

