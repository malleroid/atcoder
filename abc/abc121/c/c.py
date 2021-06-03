N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort()

ans = 0
for v in AB:
    if M-v[1] >= 0:
        ans += v[1]*v[0]
        M -= v[1]
    else:
        ans += M*v[0]
        break
print(ans)
