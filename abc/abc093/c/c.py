A, B, C = map(int, input().split())

ans = 0

if A % 2 != B % 2 or B % 2 != C % 2:

    ans += 1
    if A % 2 == B % 2:
        A += 1
        B += 1

    elif A % 2 == C % 2:
        A += 1
        C += 1

    elif B % 2 == C % 2:
        B += 1
        C += 1

n = [A, B, C]
n.sort()

ans += (n[2]-n[0])//2
ans += (n[2]-n[1])//2

print(ans)
