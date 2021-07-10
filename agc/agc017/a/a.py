N, P = map(int, input().split())
A = list(map(int, input().split()))

b = [0]*N
for i in range(N):
    b[i] = A[i] % 2

c = b.count(1)

p = 2**(c-1) if c-1 >= 1 else 0
if P == 0:

    ans = 2**N-(2**(N-c))*p
    print(ans)

else:

    ans = (2**(N-c))*p
    print(ans)
