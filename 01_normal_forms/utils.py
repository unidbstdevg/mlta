BINARY_OPERATORS = ['*', 'V', '^']


def count_binary_operators(expr):
    if expr == "":
        return float('inf')

    count = len(list(filter(lambda x: x in BINARY_OPERATORS, list(expr))))
    return count
