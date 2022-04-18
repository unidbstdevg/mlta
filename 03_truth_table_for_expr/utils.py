from binary_set import BinarySet


def make_full_list_of_binary_sets(vars_count):
    res = []

    row_set = BinarySet(vars_count)
    while True:
        row_tuple = tuple(row_set)
        res.append(row_tuple)

        if not row_set.next():
            break

    return res
