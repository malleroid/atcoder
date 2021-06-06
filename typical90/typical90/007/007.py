# 二分探索 最近傍
import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

A.sort()

for i in range(Q):
    B = int(input())

    p = bisect.bisect_left(A, B)

    num = pow(10, 18)
    if p > 0:
        num = min(num, abs(A[p-1]-B))

    if p < N:
        num = min(num, abs(A[p]-B))

    print(num)
