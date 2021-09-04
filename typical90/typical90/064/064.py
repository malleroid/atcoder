N, Q = map(int, input().split())
A = list(map(int, input().split()))

dif = [0]*(N-1)
s = 0
for i in range(N-1):
    dif[i] = A[i+1]-A[i]
    s += abs(dif[i])


for i in range(Q):
    L, R, V = map(int, input().split())
    L -= 1
    R -= 1

    if 1 <= L:
        s -= abs(dif[L-1])
        dif[L-1] += V
        s += abs(dif[L-1])

    if R <= N-2:
        s -= abs(dif[R])
        dif[R] -= V
        s += abs(dif[R])

    print(s)
