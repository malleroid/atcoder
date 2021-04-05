N = int(input())
H = list(map(int, input().split()))

ans = 0
now = 0
num = 0
while now < N-1:

    if H[now] >= H[now+1]:
        num += 1

    else:
        ans = max(ans, num)
        num = 0
    now += 1

ans = max(ans, num)
print(ans)
