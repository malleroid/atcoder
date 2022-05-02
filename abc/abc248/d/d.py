import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

d = {i: [] for i in range(1, N+1)}

for i in range(N):
    d[A[i]].append(i+1)

for v in d.values():
    v.sort()

for _ in range(Q):
    L, R, X = map(int, input().split())

    a = d[X]

    left = bisect.bisect_left(a, L)
    right = bisect.bisect_right(a, R)

    print(right-left)
