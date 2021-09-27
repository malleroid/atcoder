import itertools

N = int(input())
t = [int(input()) for _ in range(N)]

s = sum(t)
ans = 10**5
for arr in itertools.product([True, False], repeat=N):
    n = sum([t[i] * arr[i] for i in range(N)])
    ans = min(ans, max(n, s-n))

print(ans)
