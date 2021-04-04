N, M = map(int, input().split())
m = [0 for _ in range(M)]

for i in range(N):
    A = list(map(int, input().split()))
    K = A.pop(0)

    for j in range(K):
        m[A[j]-1] += 1

ans = m.count(N)
print(ans)
