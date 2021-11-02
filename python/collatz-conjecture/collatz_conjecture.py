def steps(number):
    if number < 1:
        raise ValueError("Only positive numbers are allowed")

    steps_count = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        steps_count += 1
    return steps_count


if __name__ == '__main__':
    print(steps(12))
