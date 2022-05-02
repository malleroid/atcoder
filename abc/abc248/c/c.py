N, M, K = map(int, input().split())

mod = 998244353

dp = [[0]*((M+1)*(N+1)) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(K+1):
        if dp[i][j] == 0:
            continue
        for k in range(1, M+1):
            dp[i+1][j+k] += dp[i][j]

print(sum(dp[N][:K+1]) % mod)
