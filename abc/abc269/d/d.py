N = int(input())
g = [False] * 2001 * 2001

d = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]

for i in range(N):
    X, Y = map(int, input().split())
    X += 1000
    Y += 1000

    g[X*2001+Y] = True

    for dx, dy in d:
        h = X+dx
        w = Y+dy

        if 0 <= h < 2001 and 0 <= w < 2001:
            g[h*2001+w] = True
