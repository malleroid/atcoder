S = input()
L = len(S)
p = pow(10, 9)+7

M = {'c': 0, 'h': 1, 'o': 2, 'k': 3, 'u': 4, 'd': 5, 'a': 6, 'i': 7}

dp = [[0]*L for _ in range(8)]

for i in range(L):

    if i > 0:
        for j in range(8):
            dp[j][i] = dp[j][i-1]

    if S[i] in M:

        if S[i] == 'c':
            dp[0][i] += 1

        else:

            dp[M[S[i]]][i] += dp[M[S[i]]-1][i-1]

print(dp[7][L-1] % p)
