N = int(input())
h = list(map(int, input().split()))

dp = [0]*N

for i in range(N-1):

    p = dp[i]+abs(h[i+1]-h[i])
    q = dp[max(0, i-1)]+abs(h[i+1]-h[max(0, i-1)])

    dp[i+1] = min(p, q)


print(dp[-1])
