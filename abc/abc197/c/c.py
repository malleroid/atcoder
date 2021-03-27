N = int(input())
A = list(map(int, input().split()))

ans = 2**30

for i in range(1, N):

    left = A[:i]
    right = A[i:]

    l_or = 0
    for j in range(len(left)):
        l_or = l_or | left[j]

    r_or = 0
    for k in range(len(right)):
        r_or = r_or | right[k]

    lr_xor = l_or ^ r_or

    ans = min(ans, lr_xor)

print(ans)
