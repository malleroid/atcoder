N = int(input())
A = list(map(int, input().split()))

left = 0
right = sum(A)

ans = pow(10, 13)
for i in range(N-1):

    left += A[i]
    right -= A[i]

    ans = min(ans, abs(left-right))

print(ans)
