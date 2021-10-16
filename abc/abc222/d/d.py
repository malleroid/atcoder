N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

mod = 998244353

dp = [0]*N

floor = a[0]
ceil = b[0]

dp[0] = ceil-floor+1
for i in range(1, N):
    # dp[i] = dp[i-1]
    for j in range(floor, ceil+1):
        p = max(j, a[i])
        q = b[i]

        dp[i] += q-p+1
        # print(p, q, dp)
    floor = a[i]
    ceil = b[i]
    dp[i] %= mod

print(dp[N-1])
