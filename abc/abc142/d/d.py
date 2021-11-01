import math

A, B = map(int, input().split())

x = math.gcd(A, B)


def prime_factorize(n: int) -> set:
    result = set()
    result.add(1)
    while n % 2 == 0:
        result.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            result.add(f)
            n //= f
        else:
            f += 2
    if n != 1:
        result.add(n)
    return result


primes = prime_factorize(x)

print(len(primes))
