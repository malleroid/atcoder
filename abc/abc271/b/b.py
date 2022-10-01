N, Q = map(int, input().split())

A = []
for i in range(N):
    L, *a = input().split()
    A.append(a)

for i in range(Q):
    s, t = map(int, input().split())
    print(A[s-1][t-1])
