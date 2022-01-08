import bisect

N, K = map(int, input().split())
P = list(map(int, input().split()))

p = P[:K]
p.sort()

ans = [p[-K]]*(N-K+1)

for i in range(N-K):
    n = P[K+i]
    bisect.insort(p, n)
    ans[i+1] = p[-K]

print(*ans, sep='\n')
