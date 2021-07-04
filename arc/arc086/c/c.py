import collections

N, K = map(int, input().split())
A = list(map(int, input().split()))

c = collections.Counter(A)

v = list(c.values())
v.sort()

ans = 0
for i in range(len(c)-K):

    ans += v[i]

print(ans)
