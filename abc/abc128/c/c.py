import itertools

N, M = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int, input().split()))

k = [ks[i][0] for i in range(M)]
s = [ks[i][1:] for i in range(M)]

n = [i+1 for i in range(N)]

ans = 0
for v in itertools.product([False, True], repeat=N):
    cnt_flag = True
    v = list(v)
    m = [x*y for x, y in zip(n, v)]

    for i in range(M):
        on_cnt = 0
        for j in range(k[i]):
            if m[s[i][j]-1] != 0:
                on_cnt += 1

        if on_cnt % 2 != p[i]:
            cnt_flag = False
            break

    if cnt_flag is True:
        ans += 1

print(ans)
