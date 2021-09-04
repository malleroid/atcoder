N, K = map(int, input().split())

mod = pow(10, 9)+7

if N == 1:
    print(K % mod)

elif N == 2:
    print(K*(K-1) % mod)

else:
    k = K-2
    n = N-2

    if k <= 0:
        print(0)
        exit()

    ans = K*(K-1)*pow(k, n, mod) % mod

    print(ans)
