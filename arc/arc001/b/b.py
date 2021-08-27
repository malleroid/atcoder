A, B = map(int, input().split())

ans = 0
while A != B:

    ans += 1
    if abs(B-A) >= 8:
        if B > A:
            A += 10
        else:
            A -= 10

    elif abs(B-A) >= 3:
        if B > A:
            A += 5
        else:
            A -= 5

    else:
        if B > A:
            A += 1
        else:
            A -= 1

print(ans)
