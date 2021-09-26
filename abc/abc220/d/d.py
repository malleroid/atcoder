N = int(input())
A = list(map(int, input().split()))

mod = 998244353

dp = [[0]*10 for _ in range(N)]

s = (A[0]+A[1]) % 10
m = (A[0]*A[1]) % 10

dp[1][s] += 1
dp[1][m] += 1

for i in range(2, N):
    n = A[i]

    for j in range(10):
        v = dp[i-1][j]
        s = (j+n) % 10
        m = (j*n) % 10
        dp[i][s] += v
        dp[i][m] += v

        dp[i][s] %= mod
        dp[i][m] %= mod

print(*dp[-1], sep='\n')
