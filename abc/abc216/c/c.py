N = int(input())

ans = ''
while N > 1:

    if N % 2 == 0:
        ans += 'B'
        N //= 2

    else:
        ans += 'A'
        N -= 1

ans += 'A'
print(ans[::-1])
