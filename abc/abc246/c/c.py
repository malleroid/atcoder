N, K, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if X*K <= A[i]:
        A[i] -= X*K
        K = 0
        break

    K -= A[i]//X
    A[i] %= X

A.sort(reverse=True)
for i in range(N):
    if K == 0 or A[i] == 0:
        break

    K -= 1
    A[i] = 0

print(sum(A))
