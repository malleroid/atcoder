N = int(input())
S = input()

mod = pow(10, 9)+7
d = ['a', 't', 'c', 'o', 'd', 'e', 'r']
dp = [[0]*N for _ in range(7)]

for i in range(N):

    if i > 0:
        for j in range(7):
            dp[j][i] = dp[j][i-1]

    if S[i] in d:
        s = d.index(S[i])

        if s == 0:
            dp[0][i] += 1

        else:
            dp[s][i] += dp[s-1][i]

print(dp[6][N-1] % mod)
