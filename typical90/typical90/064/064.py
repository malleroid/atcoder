# 階差を使って計算量削減, 差を左から見るのと右から見るのの区別
N, Q = map(int, input().split())
A = list(map(int, input().split()))

dif = [0]*(N-1)
s = 0
for i in range(N-1):
    dif[i] = A[i+1]-A[i]
    s += abs(dif[i])


for i in range(Q):
    L, R, V = map(int, input().split())

    if 2 <= L:
        s -= abs(dif[L-2])
        dif[L-2] += V
        s += abs(dif[L-2])

    if R <= N-1:
        s -= abs(dif[R-1])
        dif[R-1] -= V
        s += abs(dif[R-1])

    print(s)
