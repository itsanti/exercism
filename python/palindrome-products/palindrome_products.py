def largest(max_factor, min_factor=0):
    if max_factor < min_factor:
        raise ValueError("Max factor is greater than min factor")
    for n in range(max_factor ** 2, min_factor ** 2, -1):
        if is_palindrome(n):
            if len(get_factors_in_range(n, min_factor, max_factor)) == 0:
                continue
            else:
                return (n, get_factors_in_range(n, min_factor, max_factor))
    return (None, [])


def smallest(max_factor, min_factor):
    if max_factor < min_factor:
        raise ValueError("Max factor is greater than min factor")
    for n in range(min_factor ** 2, max_factor ** 2):
        if is_palindrome(n):
            if len(get_factors_in_range(n, min_factor, max_factor)) == 0:
                continue
            else:
                return (n, get_factors_in_range(n, min_factor, max_factor))
    return (None, [])


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def get_factors_in_range(num, min_factor, max_factor):
    return [(x, num // x)
            for x in range(min_factor, max_factor + 1)
            if x <= num // x
            and num % x == 0
            and num // x >= min_factor
            and num // x <= max_factor
            ]
