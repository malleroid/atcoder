A, B, C = map(int, input().split())

if A == B == C and A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    print(-1)
    exit()

cnt = 0
while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    a = A/2
    b = B/2
    c = C/2
    A = b+c
    B = c+a
    C = a+b
    cnt += 1
    if A == B == C:
        print(-1)
        exit()

print(cnt)
