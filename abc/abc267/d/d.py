N, M = map(int, input().split())
A = list(map(int, input().split()))

INF = float('inf')

dp = [[-INF]*(N+1) for _ in range(M+1)]
for i in range(N+1):
    dp[0][i] = 0

dp[1][0] = A[0]

for i in range(1, M+1):
    for j in range(i, N+1):

        dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]+A[j-1]*i)

print(dp[M][N])
