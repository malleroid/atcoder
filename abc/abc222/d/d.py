N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

mod = 998244353

dp = [[0]*3001 for _ in range(N+1)]

for i in range(3001):
    dp[0][i] = 1

for i in range(N):
    floor = a[i]
    ceil = b[i]
    for j in range(3001):
        if floor <= j <= ceil:
            dp[i+1][j] = (dp[i][j]+dp[i+1][max(0, j-1)]) % mod
        else:
            dp[i+1][j] = dp[i+1][max(0, j-1)]

print(dp[-1][-1])
