def sum_of_multiples(limit, multiples):
    if 0 in multiples:
        for zero in range(multiples.count(0)):
            multiples.remove(0)
    if 1 in multiples:
        return limit * (limit - 1) / 2
    if len(multiples) == 0:
        return 0

    result = set()
    for i in range(1, limit):
        for j in multiples:
            if i % j == 0:
                result.add(i)
    return sum(result)
