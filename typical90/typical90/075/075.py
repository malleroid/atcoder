N = int(input())

primes = []

i = 2
while i**2 <= N:

    while N % i == 0:
        primes.append(i)
        N //= i
    i += 1

if N > 1:
    primes.append(N)

print(0 if len(primes) == 1 else len(bin(len(primes)-1))-2)
