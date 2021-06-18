N, Q = map(int, input().split())
A = list(map(int, input().split()))

d_v = [0]*(N-1)
d_c = [1]*(N-1)
for i in range(N-1):
    d_c[i] = 1 if A[i+1]-A[i] >= 0 else -1
    d_v[i] = abs(A[i+1]-A[i])

s = sum(d_v)

for i in range(Q):
    L, R, V = map(int, input().split())

    if L > 1:
        v = V if d_c[L-1]*V >= 0 else abs(V-d_v[L-1])
        s += v

        d_v[L-1] = abs(v)
        d_c[L-1] = 1 if v >= 0 else -1

    if R < N:
        v = d_v[R-1]*d_c[R-1]+V

        d_v[R-1] = abs(v)
        d_c[R-1] = 1 if v >= 0 else -1
        s += v

    print(s)
