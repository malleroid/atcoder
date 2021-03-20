N, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

ans = 0
for i in range(len(a)):

    if i == len(a)-1:
        if x == a[i]:
            ans += 1
        break

    if x >= a[i]:
        ans += 1
        x -= a[i]

    else:
        break

print(ans)
