# allow to use navigation keys in input()
import readline  # noqa: F401

from binary_set import BinarySet
from expression import Expression, ExpressionParseError, ExpressionEvalError
from operators import print_operators_list

HELP_TEXT = """Expression format:
1. Expressions sets in infix notation (unary operators use prefix notation).
2. All variables should be one lower-case letter.
3. Operators are either UPPER case words, or special symbols defined as aliases.
   (for list of operators (and aliases) type 'operators' or 'list')

Some operations have priorities over others. For more details type 'priority'.
In short: there used standard and common order for most used operations.

To exit type one of: quit, exit, q"""

PRIORITY_TEXT = """Operations priority (in order from higher to lower):
1. parenthesis
2. unary operators
3. AND, NAND
4. OR, NOR
5. XOR, EQ
6. IMPL
7. all remaining binary operators"""

print(
    """This program prints truth table for logical expression entered by user.
Type 'help' or '?' for instructions and details on how to use the program.""")

expr = ""

while True:
    print("-" * 60)

    inp = input("Type expression: ")

    if inp in ("exit", "quit", "q"):
        print("Got '" + inp + "'. Goodbye!")
        exit()
    elif inp in ("help", "?"):
        print(HELP_TEXT)
        continue
    elif inp in ("priority"):
        print(PRIORITY_TEXT)
        continue
    elif inp in ("operators", "list"):
        print_operators_list()
        continue

    try:
        expr = Expression(inp)

        if len(expr.variables) < 1:
            print("Parse error: Expression must have at least one variable")
            continue

        print("Postfix notation:", expr.expr)

        try:
            row_set = (0 for x in range(len(expr.variables)))
            expr.calc(row_set)
        except ExpressionEvalError as e:
            print("Eval error:", e)
            continue
    except ExpressionParseError as e:
        print("Parse error:", e)
        continue

    # print header of truth table
    SPAN_BEFORE_F = "  "
    print("\n" + " ".join(expr.variables) + SPAN_BEFORE_F + "F")

    row_set = BinarySet(len(expr.variables))
    while True:
        f = expr.calc(tuple(row_set))
        print(str(row_set) + SPAN_BEFORE_F + str(f))

        if not row_set.next():
            break
