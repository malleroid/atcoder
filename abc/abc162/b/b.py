N = int(input())

a = [i+1 for i in range(N)]

ans = 0
for i in range(N):
    if a[i] % 3 == 0 or a[i] % 5 == 0:
        pass
    else:
        ans += a[i]

print(ans)
