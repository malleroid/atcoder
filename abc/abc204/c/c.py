import sys

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())

G = [[] for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)


def dfs(v):
    if seen[v]:
        return

    seen[v] = True
    for vv in G[v]:
        dfs(vv)


ans = 0

for i in range(N):

    seen = [False]*N

    dfs(i)

    ans += sum(seen)

print(ans)
