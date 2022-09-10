N = int(input())
p = list(map(int, input().split()))

diffs = {i: 0 for i in range(N)}

for i in range(N):
    diffs[(N-(i-p[i])) % N] += 1


ans = 0
for i in range(N):
    cnt = diffs[(N+(i-1)) % N] + diffs[i] + diffs[(i+1) % N]

    ans = max(ans, cnt)

print(ans)
