N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]
w, v = [list(i) for i in zip(*wv)]

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(N):
    for j in range(W+1):
        if j < w[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]]+v[i])

print(dp[N][W])
