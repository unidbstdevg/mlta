from expression import Expression, ExpressionParseError

while True:
    inp = input("Type expression: ")
    try:
        expr = Expression(inp)
        print("Prefix notation:", expr.expr)
        break
    except ExpressionParseError as e:
        print("Parse error:", e)
        continue
