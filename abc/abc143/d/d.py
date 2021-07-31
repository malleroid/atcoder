import bisect

N = int(input())
L = list(map(int, input().split()))

L.sort()

ans = 0
for i in range(N):
    for j in range(i+1, N):
        a = L[i]
        b = L[j]
        c = a+b

        n = bisect.bisect_left(L, c)
        ans += n-j-1

print(ans)
