def get_dual_function(results):
    inversed = inverse_function_results(results)
    res = inverse_function_arguments(inversed)

    return res


def inverse_function_results(results):
    new_results = []
    for x in results:
        new_x = 0 if x == 1 else 1
        new_results.append(new_x)

    return new_results


def inverse_function_arguments(results):
    return list(reversed(results))
