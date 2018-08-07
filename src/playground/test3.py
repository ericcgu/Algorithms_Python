    decreasing = increasing[-1]
    result = []
    for i, n in enumerate(increasing):
        if i % 2 == 0:
            result.append(decreasing[i])
        else:
            result.append(increasing[i])
    return result