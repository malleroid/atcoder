# import collections

# N, M = map(int, input().split())

# p = pow(10, 9)+7

# graph = [[] for _ in range(N+1)]

# for i in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# dist = [-1]*(N+1)
# dist[0] = 0
# dist[1] = 0

# d = collections.deque()
# d.append(1)
# print(graph)
# while d:
#     v = d.popleft()
#     for i in graph[v]:
#         print(graph[v])
#         if dist[i] != -1:
#             continue
#         dist[i] = dist[v]+1
#         d.append(i)

# dist = dist[1:]

# # print(dist)

# from collections import deque

# N, M = map(int, input().split())
# graph = [[]for _ in range(N)]
# for i in range(M):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     graph[a].append(b)
#     graph[b].append(a)

# Q = deque()
# for i in range(N):
#     Q.append(i)
#     dist = [-1 for _ in range(N)]
#     dist[i] = 0
#     while Q:
#         one = Q.popleft()
#         for j in graph[one]:
#             if dist[j] != -1:
#                 continue
#             dist[j] = dist[one]+1
#             Q.append(j)
#     print(dist)
#     # print(dist.count(2))

from heapq import heappush, heappop
INF = 10 ** 9

p = pow(10, 9)+7


def dijkstra(s, n):  # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    ans = 0
    while hq:
        v = heappop(hq)[1]  # ノードを pop する
        seen[v] = True
        for to in graph[v]:  # ノード v に隣接しているノードに対して
            if seen[to] is False and dist[v] + 1 < dist[to]:
                dist[to] = dist[v] + 1
                ans = 1
                heappush(hq, (dist[to], to))
            elif dist[v] + 1 == dist[to]:
                ans += dist[v]
    return dist, ans


N, M = map(int, input().split())
graph = [[]for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

X = dijkstra(0, N)

print(X[1] % p)
