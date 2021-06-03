N, A, B = map(int, input().split())

ans = 0

if A % 2 == B % 2:

    ans = (B-A)//2

else:

    if A-1 <= N-B:
        ans = A+(B-A)//2

    else:
        ans = N-B+1+(B-A)//2

print(ans)
