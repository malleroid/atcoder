N, L = map(int, input().split())

mod = pow(10, 9)+7
A = [1]*(N+1)

for i in range(1, N+1):
    A[i] = (A[i-1]+A[i-L]) % mod if i-L >= 0 else A[i-1]

print(A[N])
