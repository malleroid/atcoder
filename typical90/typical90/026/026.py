import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())

graph = [[] for _ in range(N)]

for i in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1

    graph[A].append(B)
    graph[B].append(A)

odd = set()
even = set()
seen = set()
i = 0
s = 0


def dfs(v, i):
    if v in seen:
        i += 1
        return

    seen.add(v)
    if i % 2 == 0 and (v+1) not in odd:
        odd.add(v+1)

        if len(odd) >= N//2:
            print(*odd, sep=' ')
            exit()

    elif i % 2 == 1 and (v+1) not in even:
        even.add(v+1)

        if len(even) >= N//2:
            print(*even, sep=' ')
            exit()
    i += 1

    for vv in graph[v]:
        dfs(vv, i)


dfs(s, i)
