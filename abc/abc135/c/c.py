N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):

    ans += min(A[i], B[i])
    if B[i] > A[i]:
        B[i] = B[i]-A[i]
        A[i] = 0

    else:
        A[i] = A[i]-B[i]
        B[i] = 0

    if B[i] > 0:
        ans += min(A[i+1], B[i])
        A[i+1] = max(0, A[i+1]-B[i])

print(ans)
