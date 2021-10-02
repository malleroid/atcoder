N = int(input())

ans = 10

for i in range(N):
    p = int(input())
    n = 0
    while p % 10 == 0:
        n += 1
        p //= 10

    ans = min(ans, n)

print(ans)
