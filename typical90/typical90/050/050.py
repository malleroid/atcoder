# DP
N, L = map(int, input().split())

A = [1]*(N+1)

for i in range(N+1):
    A[i] *= A[i-1] if i-1 >= 0 else 1
    A[i] += A[i-L] if i-L >= 0 else 0

print(A[N] % (pow(10, 9)+7))
