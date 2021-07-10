N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]

T.sort()

ans = 1
psg = 0
time = T[0]
for i in range(N):

    if time+K >= T[i] and psg < C:
        psg += 1

    else:
        ans += 1
        psg = 1
        time = T[i]

print(ans)
