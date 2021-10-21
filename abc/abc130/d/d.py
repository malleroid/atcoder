N, K = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
now = 0
left = 0
right = 0
for i in range(N):
    now += a[i]

    while now >= K:
        now -= a[left]
        left += 1

    ans += left

print(ans)
