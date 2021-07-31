import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = float('INF')
for i in range(N):

    p = bisect.bisect_left(B, A[i])

    left = B[p-1] if p > 0 else float('INF')
    right = B[p] if p < M else float('INF')

    num = min(abs(left-A[i]), abs(right-A[i]))

    ans = min(ans, num)

    if ans == 0:
        print(ans)
        exit()

print(ans)
