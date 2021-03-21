N = int(input())

ans = 0
d = 2

while d <= len(str(N)):
    if d % 2 == 0 and d == len(str(N)):
        m = str(N)
        left = m[:d//2]
        right = m[d//2:]
        if int(left) <= int(right):
            ans += int(left)-10**(d//2-1)+1

        else:
            ans += int(left)-10**(d//2-1)

    elif d % 2 == 0:
        ans += 9*10**(d//2-1)

    d += 2

print(ans)
