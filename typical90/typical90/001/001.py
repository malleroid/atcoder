N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

a = [0]+A+[L]
d = [0]*(N+1)
for i in range(N+1):
    d[i] = a[i+1]-a[i]

left = 0
right = L
K += 1
while right - left > 1:
    mid = (right+left)//2
    num = mid
    cnt = 0
    p = 0

    for i in range(N+1):
        p += d[i]
        if p >= num:
            cnt += 1
            p = 0

    if cnt < K:
        right = mid

    else:
        left = mid

print(left)
