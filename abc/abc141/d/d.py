import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    A[i] *= (-1)

heapq.heapify(A)

for i in range(M):
    p = abs(heapq.heappop(A))
    p //= 2
    heapq.heappush(A, -p)

print(-sum(A))
