import collections
import sys

sys.setrecursionlimit(10 ** 6)

N, Q = map(int, input().split())

graph = [[0, 0] for _ in range(N+1)]

for i in range(Q):
    n, *s = map(int, input().split())

    if n == 1:
        graph[s[0]][1] = s[1]
        graph[s[1]][0] = s[0]

    elif n == 2:
        graph[s[0]][1] = 0
        graph[s[1]][0] = 0

    elif n == 3:
        q = collections.deque()
        if graph[s[0]][0] != 0:
            q.appendleft(graph[s[0]][0])
        ans = collections.deque()
        ans.appendleft(s[0])
        m = 1
        while q:
            p = q.pop()
            ans.appendleft(p)
            m += 1
            if graph[p][0] != 0:
                q.appendleft(graph[p][0])

        if graph[s[0]][1] != 0:
            q.append(graph[s[0]][1])
        while q:
            p = q.pop()
            ans.append(p)
            m += 1
            if graph[p][1] != 0:
                q.append(graph[p][1])

        print(m, *ans, sep=' ')
