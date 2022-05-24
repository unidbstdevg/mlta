from utils import make_full_list_of_binary_sets

operators = {}
# after init, operators would be dict where key is operator name, and value is
# corresponding truth_table:
# binary_operators[operator_name] = TruthTable
# where TruthTable is tuple

UNARY_OPERATORS = ["UNARY_CONSTANT_0", "NOP", "NOT", "UNARY_CONSTANT_1"]
# truth table            name
# 0 0                    UNARY_CONSTANT_0
# 0 1                    NOP
# 1 0                    NOT
# 1 1                    UNARY_CONSTANT_1

BINARY_OPERATORS_WITH_PRIORITY = {
    "BINARY_CONSTANT_0": 0,
    "AND": 4,
    "GREATER": 0,
    "OPERAND_1": 0,
    "LESSER": 0,
    "OPERAND_2": 0,
    "XOR": 2,
    "OR": 3,
    "NOR": 3,
    "EQ": 2,
    "NOT_OPERAND_2": 0,
    "REVERSE_IMPL": 0,
    "NOT_OPERAND_1": 0,
    "IMPL": 1,
    "NAND": 4,
    "BINARY_CONSTANT_1": 0
}
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

OPERATORS_ALIASES = {
    "NOT": ["!"],
    "AND": ["*", "&"],
    "OR": ["+", "V", "U"],
    "XOR": ["^"],
    "IMPL": ["->", "=>"],
    "REVERSE_IMPL": ["<-", "<="],
    "EQ": ["=", "=="],
}


def get_raw_operator_name(name):
    if name in UNARY_OPERATORS or name in BINARY_OPERATORS_WITH_PRIORITY:
        return name

    for raw_name, aliases in OPERATORS_ALIASES.items():
        if name in aliases:
            return raw_name

    return None


def init_operators():
    # construct unary operators
    unary_operators_tables = make_full_list_of_binary_sets(2)
    unary_operators = dict(zip(UNARY_OPERATORS, unary_operators_tables))

    # construct binary operators
    binary_operators_tables = make_full_list_of_binary_sets(4)
    binary_operators = dict(
        zip(BINARY_OPERATORS_WITH_PRIORITY.keys(), binary_operators_tables))

    global operators
    operators.update(unary_operators)
    operators.update(binary_operators)


def is_operator(name):
    name = get_raw_operator_name(name)
    return name in operators.keys()


def operands_count(operator):
    operator = get_raw_operator_name(operator)

    if operator in UNARY_OPERATORS:
        return 1
    elif operator in BINARY_OPERATORS_WITH_PRIORITY:
        return 2

    return None


def get_operator_priority(name):
    name = get_raw_operator_name(name)

    # all unary operators have priority over binary operators
    if name in UNARY_OPERATORS:
        return 100

    return BINARY_OPERATORS_WITH_PRIORITY[name]


def apply_operator(operator_name, operands):
    operator_name = get_raw_operator_name(operator_name)

    # reverse operands order (to match real operands order)
    operands.reverse()

    truth_table = operators[operator_name]
    # TODO: check not null

    num = int("".join(operands), 2)

    return truth_table[num]


def print_operators_list():
    print("Format: truth_table operator_name (aliases)")
    categories = {
        "Unary operators:": UNARY_OPERATORS,
        "Binary operators:": BINARY_OPERATORS_WITH_PRIORITY.keys()
    }
    for category, opers in categories.items():
        print("\n" + category)
        for x in opers:
            s = "\t" + "".join(str(v) for v in operators[x]) + " " + x
            if x in OPERATORS_ALIASES:
                s += " (aliases: " + ", ".join(OPERATORS_ALIASES[x]) + ")"
            print(s)


init_operators()
