import bisect

n = int(input())
a = list(map(int, input().split()))

a.sort()

if n == 2:
    print(a[1], a[0])
    exit()

num = a[-1]//2
idx = bisect.bisect_left(a, num)

if abs(a[idx-1]-num) < abs(a[idx]-num):
    print(a[-1], a[idx-1])
else:
    print(a[-1], a[idx])
