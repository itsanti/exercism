def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min > max")
    min_product = min_factor ** 2 - 1
    result = [min_product, []]
    for i in range(min_factor, max_factor + 1):
        for j in range(max_factor, i - 1, -1):
            if is_palindrome2(i * j) and i * j >= min_product:
                min_product = i * j
                if result[0] != min_product:
                    result = (min_product, [])
                result[1].append([i, j])
    if len(result[1]) == 0:
        result[0] = None
    return tuple(result)


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min > max")
    max_product = max_factor ** 2 + 1
    result = [max_product, []]
    for i in range(min_factor, max_factor + 1):
        for j in range(max_factor, i - 1, -1):
            if is_palindrome2(i * j) and i * j <= max_product:
                max_product = i * j
                if result[0] != max_product:
                    result = (max_product, [])
                result[1].append([i, j])
    if len(result[1]) == 0:
        result[0] = None
    return tuple(result)


def is_palindrome2(number):
    stg = str(number)
    return stg == stg[::-1]


def is_palindrome(number):
    str_number = str(number)
    if len(str_number) < 2:
        return True
    for i in range(len(str_number) // 2):
        if str_number[i] != str_number[-i - 1]:
            return False
    return True


if __name__ == "__main__":
    print(largest(min_factor=15, max_factor=15))
    print(largest(min_factor=1, max_factor=9)) # 9, [[1, 9], [3, 3]]

