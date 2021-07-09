N, P = map(int, input().split())
A = list(map(int, input().split()))

b = [0]*N
for i in range(N):
    b[i] = A[i] % 2

c = b.count(1)

num = (N-c)*(c//2)
