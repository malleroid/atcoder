H = int(input())

ans = 0

t = 1
while H > 0:

    ans += t
    H = H//2
    t = t*2

print(ans)
