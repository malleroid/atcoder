import math

N, M = map(int, input().split())

p = pow(10, 9)+7

if abs(N-M) >= 2:
    print(0)

else:
    if N == M:
        ans = (math.factorial(N) % p*math.factorial(M) % p)*2 % p

    else:
        ans = (math.factorial(N) % p*math.factorial(M) % p) % p

    print(ans)
