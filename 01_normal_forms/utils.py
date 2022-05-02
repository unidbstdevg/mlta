BINARY_OPERATORS = ['*', 'V', '^']


def count_binary_operators(expr):
    return len(list(filter(lambda x: x in BINARY_OPERATORS, list(expr))))
