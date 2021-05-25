A, B, C, X, Y = map(int, input().split())

ans = 0

if A+B <= 2*C:
    ans = A*X+B*Y

else:
    ans += 2*C*min(X, Y)

    if X >= Y:
        ans += min((X-Y)*2*C, (X-Y)*A)

    else:
        ans += min((Y-X)*2*C, (Y-X)*B)

print(ans)
