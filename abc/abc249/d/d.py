N = int(input())
A = list(map(int, input().split()))

M = max(A)

a = [0]*(3*10**5)

for i in range(N):
    a[A[i]] += 1

ans = 0
for i in range(1, M+1):
    for j in range(1, M//i+1):
        k = i*j
        ans += a[i]*a[j]*a[k]

print(ans)
