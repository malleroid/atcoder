N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

ss = set(S)
st = set(T)

if ss >= st:
    pass

else:
    print(-1)
    exit()

dist = 0
if len(ss) == 2:
    v = 1 ^ S[0]
    rs = S[::-1]

    dist = min(S.index(v)-1, rs.index(v))

ans = 0
move = False
now = S[0]
for i in range(M):
    if now == T[i]:
        ans += 1

    else:
        if move is False:
            move = True
            ans += dist

        ans += 2
        now ^= 1

print(ans)
