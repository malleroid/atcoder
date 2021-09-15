# ランクなしシンプル版
parents = [-1]*N


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
