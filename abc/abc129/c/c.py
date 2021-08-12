N, M = map(int, input().split())

mod = pow(10, 9)+7

a = [True]*N

for i in range(M):
    b = int(input())
    b -= 1
    a[b] = False

dp = [0]*N

for i in range(N):
    if a[i] is True:

        if i == 0:
            dp[i] = 1

        elif i == 1:
            dp[i] = dp[0]+1

        else:
            dp[i] = dp[i-1]+dp[i-2]
            dp[i] %= mod
    else:
        dp[i] = 0

print(dp[N-1])
