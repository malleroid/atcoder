N = int(input())

tree = [[0]*N for _ in range(N)]

for i in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    tree[u][v] = w
    tree[v][u] = w

print(tree)
