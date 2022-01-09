import heapq
N, K = map(int, input().split())
P = list(map(int, input().split()))

p = P[:K]

heapq.heapify(p)
ans = [p[-K]]*(N-K+1)
for i in range(N-K):
    n = P[K+i]
    heapq.heappushpop(p, n)
    ans[i+1] = p[-K]

print(*ans, sep='\n')
