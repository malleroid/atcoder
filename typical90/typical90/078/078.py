N, M = map(int, input().split())

graph = [0 for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a > b:
        a, b = b, a

    graph[b] += 1

print(graph.count(1))
