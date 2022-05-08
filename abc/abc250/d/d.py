import bisect


def eratosthenes(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * 2, n + 1, i):
                prime[j] = False
    return [i for i in range(n + 1) if prime[i]]


N = int(input())

primes = eratosthenes(10**6)

ans = 0

for p in primes:
    q = p**3

    cube_root = min(N//q, p-1)

    n = bisect.bisect_right(primes, cube_root)

    ans += n

print(ans)
