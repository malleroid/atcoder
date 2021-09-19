import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]

graph = [[] for _ in range(N)]

for i in range(N-1):
    A, B = AB[i][0]-1, AB[i][1]-1

    graph[A].append(B)
    graph[B].append(A)

# print(graph)

s = 0
for i in range(N):
    if len(graph[i]) == 1:
        s = i
        break

print(s)

ans = []
seen = []
def dfs(v):
