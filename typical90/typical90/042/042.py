K = int(input())

mod = pow(10, 9)+7

if K % 9 != 0:
    print(0)

else:
    dp = [0]*(K+1)
    dp[0] = 1

    for i in range(1, K+1):
        r = min(i, 9)
        for j in range(1, r+1):
            dp[i] += dp[i-j]

    print(dp[K] % mod)
