N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
cd = [list(map(int, input().split())) for _ in range(M)]

for v in ab:

    num = pow(10, 9)
    ans = 0

    for i, vv in enumerate(cd):
        d = abs(vv[0]-v[0])+abs(vv[1]-v[1])

        if d < num:
            num = d
            ans = i+1

    print(ans)
