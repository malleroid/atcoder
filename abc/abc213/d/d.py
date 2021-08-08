import sys
sys.setrecursionlimit(10**7)

N = int(input())

graph = [[-1]*N for _ in range(N)]

for i in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1

    graph[A][B] = B
    graph[B][A] = A

print(graph)

hist = ''
visited = [False]*N
now = 0
root = 0


def dfs(graph, node):
    global visited
    global hist
    if visited[node] is False:
        visited[node] = True
        hist += str(node+1)
        for n in graph[node]:
            if n >= 0:
                dfs(graph, n)

                hist += str(n+1)+'p'


dfs(graph, now)

print(hist)
