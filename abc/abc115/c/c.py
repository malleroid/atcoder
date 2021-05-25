N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]

h.sort(reverse=True)

ans = 10**9
for i in range(N-K+1):
    ans = min(ans, h[i]-h[i+K-1])

print(ans)
