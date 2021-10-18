import heapq

N, M = map(int, input().split())

indeg = [0]*(N+1)
outdeg = {i: [] for i in range(1, N+1)}

for i in range(M):
    A, B = map(int, input().split())
    indeg[B] += 1
    outdeg[A].append(B)

hq = []
heapq.heapify(hq)

num = 0
for i in range(1, N+1):
    if indeg[i] == 0:
        heapq.heappush(hq, i)
        num += 1

S = []
while hq:
    p = heapq.heappop(hq)
    S.append(p)

    for e in outdeg[p]:
        indeg[e] -= 1
        if indeg[e] == 0:
            heapq.heappush(hq, e)
            num += 1

if num != N:
    print(-1)

else:
    print(*S, sep=' ')
