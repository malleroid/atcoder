import collections

N = int(input())

graph = [[] * N for _ in range(N)]
for i in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

d = 1
a = [-1]*N
a[0] = 0
q = collections.deque()
res_q = collections.deque()
s_index = 0

for v in graph[0]:
    q.append(v)

while q or res_q:
    p = q.popleft()
    if a[p] == -1:
        a[p] = d
        s_index = p
        for v in graph[p]:
            res_q.append(v)

    if not q:
        for v in res_q:
            q.append(v)
        res_q.clear()
        d += 1

b = [-1]*N
b[s_index] = 0
d = 1
for v in graph[s_index]:
    q.append(v)

while q or res_q:
    p = q.popleft()
    if b[p] == -1:
        b[p] = d
        s_index = p
        for v in graph[p]:
            res_q.append(v)

    if not q and res_q:
        for v in res_q:
            q.append(v)
        res_q.clear()
        d += 1

print(d)
