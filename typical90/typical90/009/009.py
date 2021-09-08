import collections

N, M = map(int, input().split())
ST = [list(map(int, input().split())) for _ in range(M)]

emp = [0]*N
a = [-1]*N
q = collections.deque()

cnt = 0
for i in range(M):
    if ST[i][0] == ST[i][1]:
        cnt += 1

    ST[i][0] -= 1
    ST[i][1] -= 1

    emp[ST[i][0]] = 1

    a[ST[i][1]] = ST[i][0]

for i in range(N):
    if emp[i] == 0:
        q.append(i)

while q:
    p = q.popleft()
    if a[p] != -1:
        q.append(a[p])
        cnt += 1

print('Yes' if cnt != M else 'No')
