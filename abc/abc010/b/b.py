n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):

    if (a[i]-1) % 6 == 1 or (a[i]-1) % 6 == 3:
        ans += 1

    elif (a[i]-1) % 6 == 4:
        ans += 2

    elif (a[i]-1) % 6 == 5:
        ans += 3

print(ans)
