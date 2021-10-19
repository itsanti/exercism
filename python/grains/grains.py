def square(number):
    if number < 1:
        raise ValueError("square number must be positive")
    elif number > 64:
        raise ValueError("square number must be less then 64")
    return 2 ** (number - 1)


def total():
    return 2 ** 64 - 1
