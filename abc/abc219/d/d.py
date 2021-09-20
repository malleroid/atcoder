N = int(input())
X, Y = map(int, input().split())

INF = N+1

dp = [[INF]*(Y+1) for _ in range(X+1)]

dp[0][0] = 0
for _ in range(N):
    a, b = map(int, input().split())

    for i in range(X, -1, -1):

        for j in range(Y, -1, -1):
            pi = min(i+a, X)
            pj = min(j+b, Y)
            dp[pi][pj] = min(dp[i][j]+1, dp[pi][pj])

print(dp[X][Y] if dp[X][Y] < INF else -1)
