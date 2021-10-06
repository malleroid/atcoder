import collections

N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [0]*N
q = collections.deque()
k = 0
for i in range(1, N):
    if k < K:
        k += 1
    else:
        q.popleft()

    q.append(h[i-1])

    m = list(q)
    n = pow(10, 9)
    p = 0
    for j, v in enumerate(m):
        n = min(n, dp[i-k+j]+abs(h[i]-v))

    dp[i] = n

print(dp[-1])
