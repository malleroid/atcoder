H, W = map(int, input().split())
Q = int(input())

g = [False]*H*W


parents = [-1]*H*W


def find(x):
    if parents[x] < 0:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]


def unite(x, y):
    par_x = find(x)
    par_y = find(y)
    if par_x == par_y:
        return

    if par_x > par_y:
        par_x, par_y = par_y, par_x

    parents[par_x] += parents[par_y]
    parents[par_y] = par_x


def same(x, y):
    return find(x) == find(y)


d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for i in range(Q):
    t, *q = map(int, input().split())

    if t == 1:
        r = q[0]-1
        c = q[1]-1

        g[r*W+c] = True

        for dh, dw in d:
            h = r+dh
            w = c+dw

            if 0 <= h < H and 0 <= w < W and g[h*W+w]:
                unite(r*W+c, h*W+w)

    elif t == 2:
        ra = q[0]-1
        ca = q[1]-1
        rb = q[2]-1
        cb = q[3]-1

        if g[ra*W+ca] and g[rb*W+cb] and same(ra*W+ca, rb*W+cb):
            print('Yes')

        else:
            print('No')
