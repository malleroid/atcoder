import copy

N, M, Q = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
WV.sort(reverse=True)
X = list(map(int, input().split()))

for i in range(Q):
    L, R = map(int, input().split())
    # print(X[:L-1], X[R:], sep=' ')
    x = X[:L-1]+X[R:]
    x.sort(reverse=True)
    wv = copy.copy(WV)
    ans = 0
    while len(x) > 0 and len(wv) > 0:
        if x[0] >= wv[0][0]:
            ans += wv[0][1]
            x.pop(0)
            wv.pop(0)
        else:
            wv.pop(0)
    print(ans)
