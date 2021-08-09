import sys
sys.setrecursionlimit(10**7)

N = int(input())

graph = [[]*N for _ in range(N)]

for i in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

for i in range(N):
    graph[i].sort()

hist = []
visited = [False]*N


def euler_tour(now, bef):
    global visited
    global hist
    hist += [now+1]
    for e in graph[now]:
        if e != bef:
            euler_tour(e, now)
            hist += [now+1]


euler_tour(0, -1)

print(*hist)
