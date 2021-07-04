N, K = map(int, input().split())

ans = 0
k = len(bin(K)[2:])

for i in range(1, N+1):

    num = 0
    while i < K:
        num += 1
        i *= 2

    ans += 1/(N*2**num)

print(ans)
