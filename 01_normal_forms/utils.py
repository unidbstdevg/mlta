BINARY_OPERATORS = ['*', 'V', '^']


def count_binary_operators(expr):
    count = len(list(filter(lambda x: x in BINARY_OPERATORS, list(expr))))
    if count <= 0:
        count = float('inf')

    return count
