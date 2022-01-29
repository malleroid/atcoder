se = [list(map(int, input().split())) for _ in range(3)]

ans = 0
for i in range(3):
    s, e = se[i]
    ans += s//10*e

print(ans)
