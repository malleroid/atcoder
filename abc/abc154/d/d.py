N, K = map(int, input().split())
p = list(map(int, input().split()))

expv = [0]*N

for i in range(N):
    expv[i] = (p[i]+1)/2

expsum = [0]*N
now = 0
for i in range(N):
    now += expv[i]
    expsum[i] = now

ans = 0
for i in range(N-K+1):
    num = expsum[i+K-1]-expsum[i-1] if i > 0 else expsum[i+K-1]
    ans = max(ans, num)

print(ans)
