def primes(limit):
    sieve = list(range(2, limit + 1))

    for d in range(0, len(sieve)):
        if sieve[d] is not None:
            sieve[2 * sieve[d] - 2::sieve[d]] = [None] * len(sieve[2 * sieve[d] - 2::sieve[d]])
    return [prime for prime in sieve if prime is not None]


if __name__ == '__main__':
    print(primes(10))
