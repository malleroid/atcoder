N = int(input())
a = list(map(int, input().split()))

s = sum(a)-a[0]
snuke = a[0]
ans = abs(s-snuke)
for i in range(1, N-1):
    snuke += a[i]
    s -= a[i]

    ans = min(ans, abs(s-snuke))

print(ans)
