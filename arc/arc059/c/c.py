N = int(input())
a = list(map(int, input().split()))

num = float('inf')
for i in range(-100, 101):

    cnt = 0
    for j in range(N):
        cnt += abs(a[j]-i)**2

    num = min(num, cnt)

print(num)
