import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

A.sort()

for i in range(Q):
    B = int(input())

    p = bisect.bisect_left(A, B)
    num = pow(10, 10)

    if p != 0:
        num = min(num, abs(A[p-1]-B))

    if p != N:
        num = min(num, abs(A[p]-B))

    print(num)
