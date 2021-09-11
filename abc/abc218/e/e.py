N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N)]

ans = 0
for i in range(M):
    ABC[i][0] -= 1
    ABC[i][1] -= 1
    a, b, c = ABC[i][0], ABC[i][1], ABC[i][2]

    if a != b:
        graph[a].append(b)
        graph[b].append(a)

    else:
        if c > 0:
            ans += c

ABC.sort(reverse=True, key=lambda x: x[2])
for i in range(M):
    a, b, c = ABC[i][0], ABC[i][1], ABC[i][2]

    if a == b:
        continue

    if c < 0:
        break

    if len(graph[a]) >= 2 and len(graph[b]) >= 2:
        ans += c
        graph[a].remove(b)
        graph[b].remove(a)

print(graph)
print(ans)
