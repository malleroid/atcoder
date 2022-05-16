N = int(input())
A = list(map(int, input().split()))

dp1 = [float('inf')]*(N+1)
dp2 = [float('inf')]*(N)

dp1[1] = dp1[2] = A[0]
dp2[0] = dp2[1] = A[N-1]

for i in range(3, N+1):
    dp1[i] = min(dp1[i-1]+A[i-1], dp1[i-2]+A[i-2])

for i in range(2, N):
    dp2[i] = min(dp2[i-1]+A[i-1], dp2[i-2]+A[i-2])

print(min(dp1[N], dp2[N-1]))
