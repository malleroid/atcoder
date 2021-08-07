N, si, sj = map(int, input().split())
c = [list(input()) for _ in range(N)]

dp = [[False]*N for _ in range(N)]

for i in range(N):

    for j in range(N):
        if c[i][j] == '#':
            dp[i][j] = True
