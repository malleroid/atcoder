import collections

N, M = map(int, input().split())

mod = pow(10, 9)+7

graph = [[]*N for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

# print(graph)

dist = [-1]*N
dist[0] = 0
q = collections.deque()
q.append(0)

hist = []

while q:
    v = q.popleft()
    hist.append(v)
    for e in graph[v]:
        if dist[e] >= 0:
            continue
        dist[e] = dist[v]+1
        q.append(e)

# print(dist)

dp = [0]*N
dp[0] = 1

for x in hist:
    for y in graph[x]:
        if dist[y] == dist[x]+1:
            dp[y] += dp[x]

print(dp[N-1] % mod)
