import itertools

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

p = {}
X = [0]*N
Y = [0]*N
for i in range(N):
    x, y = xy[i][0], xy[i][1]
    X[i] = x
    Y[i] = y
    p.setdefault(x, []).append(i)

ans = 0
for p1, p2 in itertools.combinations(p.items(), 2):
    if len(p1[1]) < 2 or len(p2[1]) < 2:
        continue

    p2y = set()
    for v in p2[1]:
        p2y.add(Y[v])

    for x1, x2 in itertools.combinations(p1[1], 2):
        p1y1 = Y[x1]
        p1y2 = Y[x2]

        if p1y1 in p2y and p1y2 in p2y:
            ans += 1

print(ans)
