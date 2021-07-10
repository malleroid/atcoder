N = int(input())
A = list(map(int, input().split()))

A.insert(0, 0)
A.append(0)

B = [0]*(N+1)

for i in range(N+1):
    B[i] = abs(A[i+1]-A[i])

s = sum(B)
for i in range(N):
    ans = s-B[i]-B[i+1]+abs(A[i+2]-A[i])
    print(ans)
