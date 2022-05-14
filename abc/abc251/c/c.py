N = int(input())
ST = [list(input().split()) for _ in range(N)]

ans = 0
num = 0
set_s = set()

for i in range(N):
    S, T = ST[i]
    T = int(T)

    if S in set_s:
        continue

    set_s.add(S)

    if T > num:
        num = T
        ans = i+1

print(ans)
