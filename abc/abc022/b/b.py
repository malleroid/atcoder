N = int(input())
A = [int(input())-1 for _ in range(N)]

a = [0]*pow(10, 5)

ans = 0
for i in range(N):
    ans += a[A[i]]
    a[A[i]] = 1

print(ans)
