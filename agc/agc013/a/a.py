N = int(input())
A = list(map(int, input().split()))

ans = 1
now = None
for i in range(N-1):

    if now is None:
        if A[i+1] > A[i]:
            now = True
        elif A[i+1] < A[i]:
            now = False

    elif now is True:
        if A[i+1] < A[i]:
            now = None
            ans += 1

    elif now is False:
        if A[i+1] > A[i]:
            now = None
            ans += 1

print(ans)
