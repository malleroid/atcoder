N = int(input())

ss = []
for i in range(N):
    s = list(input())
    s.sort()
    ss.append(s)

ss.sort()
ans = 0
now = 1

for i in range(N-1):
    if ss[i+1] == ss[i]:
        now += 1
        if i == N-2:
            ans += now*(now-1)//2

    else:
        ans += now*(now-1)//2
        now = 1

print(ans)
