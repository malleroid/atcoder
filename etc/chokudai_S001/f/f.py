N = int(input())
A = list(map(int, input().split()))

ans = 0
a_max = 0

for i in range(N):
    if A[i] > a_max:
        ans += 1
        a_max = A[i]

print(ans)
