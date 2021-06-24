N, T = map(int, input().split())
t = list(map(int, input().split()))

ans = 0
now = 0
for i in range(N):
    if now == 0:
        now += T
        ans += T

    else:
        if t[i]-t[i-1] >= now:
            now = 0
        else:
            now -= now-(t[i]-t[i-1])
            ans -= T-(t[i]-t[i-1])
        now += T
        ans += T

print(ans)
