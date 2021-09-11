H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]

dp = [[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i == 0:
            if j > 0:
                dp[i][j] = dp[i][j-1] if s[i][j-1] == s[i][j] else dp[i][j-1]+1

        else:
            if j == 0:
                dp[i][j] = dp[i-1][j] if s[i-1][j] == s[i][j] else dp[i-1][j]+1

            else:
                upper = dp[i-1][j] if s[i-1][j] == s[i][j] else dp[i-1][j]+1
                left = dp[i][j-1] if s[i][j-1] == s[i][j] else dp[i][j-1]+1
                dp[i][j] = min(upper, left)

num = dp[H-1][W-1]
if s[0][0] == '#' or s[H-1][W-1] == '#':
    num += 1

print((num+1)//2)
