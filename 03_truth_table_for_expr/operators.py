from utils import make_full_list_of_binary_sets

operators = {}
# after init, operators would be dict where key is operator name, and value is
# corresponding truth_table:
# binary_operators[operator_name] = TruthTable
# where TruthTable is tuple

UNARY_OPERATORS = ["NOT"]

BINARY_OPERATORS = [
    "BINARY_CONSTANT_0", "AND", "GREATER", "OPERAND_1", "LESSER", "OPERAND_2",
    "XOR", "OR", "NOR", "EQ", "NOT_OPERAND_2", "REVERSE_IMPL", "NOT_OPERAND_1",
    "IMPL", "NAND", "BINARY_CONSTANT_1"
]
# truth table            name
# 0 0 0 0                BINARY_CONSTANT_0
# 0 0 0 1                AND
# 0 0 1 0                GREATER
# 0 0 1 1                OPERAND_1
# 0 1 0 0                LESSER
# 0 1 0 1                OPERAND_2
# 0 1 1 0                XOR
# 0 1 1 1                OR
# 1 0 0 0                NOR
# 1 0 0 1                EQ
# 1 0 1 0                NOT_OPERAND_2
# 1 0 1 1                REVERSE_IMPL
# 1 1 0 0                NOT_OPERAND_1
# 1 1 0 1                IMPL
# 1 1 1 0                NAND
# 1 1 1 1                BINARY_CONSTANT_1


def init_operators():
    unary_operators = {"NOT": (1, 0)}

    # construct binary operators
    binary_operators_tables = make_full_list_of_binary_sets(4)
    binary_operators = dict(zip(BINARY_OPERATORS, binary_operators_tables))

    global operators
    operators.update(unary_operators)
    operators.update(binary_operators)


def is_operator(name):
    return name in operators.keys()


def operands_count(operator):
    if operator in UNARY_OPERATORS:
        return 1
    elif operator in BINARY_OPERATORS:
        return 2

    return None


def apply_operator(operator_name, operands):
    truth_table = operators[operator_name]
    # TODO: check not null

    num = int("".join(operands), 2)

    return truth_table[num]


init_operators()
