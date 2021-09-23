N = int(input())

imos = [[0]*1000 for _ in range(1000)]
field = [[0]*1000 for _ in range(1000)]

for i in range(N):
    lx, ly, rx, ry = map(int, input().split())

    imos[ly][lx] += 1
    if rx < 1000:
        imos[ly][rx] -= 1
    if ry < 1000:
        imos[ry][lx] -= 1
        if rx < 1000:
            imos[ry][rx] += 1

for i in range(1000):
    v = 0
    for j in range(1000):
        v += imos[i][j]
        field[i][j] = field[max(0, i-1)][j]+v

cnt = [0]*(N+1)
for i in range(1000):
    for j in range(1000):
        cnt[field[i][j]] += 1

print(*cnt[1:], sep='\n')
