m, n, N = map(int, input().split())

rem = N
ans = N

while rem >= m:

    reuse = rem//m*n
    ans += reuse
    rem = rem % m
    rem += reuse

print(ans)
