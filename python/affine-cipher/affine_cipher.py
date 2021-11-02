import string
m = 26


def encode(plain_text: str, a, b):
    global m

    if not is_coprime(a, m):
        raise ValueError("a and m must be coprime.")

    plain_text = plain_text.lower()
    encoded = ' '

    for char in plain_text:
        if char == ' ' or char in string.punctuation:
            continue
        elif char.isdigit():
            encoded += char
        else:
            ix = (a * string.ascii_lowercase.index(char) + b) % m
            encoded += string.ascii_lowercase[ix]
        if len(encoded) % 6 == 0:
            encoded += ' '
    return encoded.strip()


def decode(ciphered_text, a, b):
    global m
    decoded = ''
    localmmi = mmi(a)

    if not is_coprime(a, m):
        raise ValueError("a and m must be coprime.")

    for char in ciphered_text:
        if char.isdigit():
            decoded += char
        elif char != ' ':
            ix = (localmmi * (string.ascii_lowercase.index(char) - b)) % m
            decoded += string.ascii_lowercase[ix]
    return decoded


def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return gcd(x, y) == 1


def mmi(a):
    global m
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x
    return -1


if __name__ == '__main__':
    print(encode("no", 15, 18))  # "fu"
    print(decode("tytgn fjr", 3, 7))  # "exercism"
    # "swxtj npvyk lruol iejdc blaxk swxmh qzglf"
    print(encode("The quick brown fox jumps over the lazy dog.", 17, 33))
