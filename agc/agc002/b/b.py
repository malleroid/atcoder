N, M = map(int, input().split())

c = [1]*N
d = {i: 1 if i == 0 else 0 for i in range(N)}

for i in range(M):
    x, y = map(int, input().split())

    x -= 1
    y -= 1

    c[x] -= 1
    c[y] += 1

    if d[x] == 1:
        d[y] = 1

    if c[x] == 0:
        d[x] = 0

ans = 0
for i in range(N):
    if c[i] >= 1 and d[i] == 1:
        ans += 1

print(ans)
