N, K = map(int, input().split())

mod = pow(10, 9)+7

if N == 1:
    print(K % mod)

elif N == 2:
    print(K*(K-1) % mod)

else:
    k = max(K-2, 0)
    n = N-2
    ans = K*(K-1) % mod if k > 0 else 0

    s = bin(n)
    s = s[2:]
    s = s[::-1]

    for i, v in enumerate(s):
        if v != '0':
            num = k**(2**i) % mod
            ans = ans*num % mod

    print(ans)
