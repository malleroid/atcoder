N = int(input())

a = [0 for _ in range(6)]

for i in range(N):

    M, m = map(float, input().split())

    if M >= 35:
        a[0] += 1

    elif 30 <= M < 35:
        a[1] += 1

    elif 25 <= M < 30:
        a[2] += 1

    elif M < 0:
        a[5] += 1

    if m >= 25:
        a[3] += 1

    if m < 0 and M >= 0:
        a[4] += 1

print(*a)
