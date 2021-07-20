import collections

N = int(input())
a = list(map(int, input().split()))

c = collections.Counter(a)

ans = 0
for k, v in c.items():

    if k > v:
        ans += v

    elif v > k:
        ans += v-k

print(ans)
