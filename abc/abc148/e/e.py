N = int(input())

ans = 0
if N % 2 != 0:
    print(ans)

else:
    m = 2
    while N >= m:
        m *= 5
        ans += N//m

    print(ans)
