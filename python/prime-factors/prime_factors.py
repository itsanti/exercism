def factors(value):
    result = []
    div = 2
    while value > 1:
        while value % div == 0:
            result.append(div)
            value //= div
        div += 1
    return result


if __name__ == '__main__':
    print(factors(60))
