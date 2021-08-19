import collections

n = int(input())
v = list(map(int, input().split()))

v1 = [v[i] for i in range(n) if i % 2 == 0]
v2 = [v[i] for i in range(n) if i % 2 == 1]

c1 = collections.Counter(v1)
c2 = collections.Counter(v2)

c1 = sorted(c1.items(), reverse=True, key=lambda x: x[1])
c2 = sorted(c2.items(), reverse=True, key=lambda x: x[1])

ans = 0
if len(c1) == len(c2) == 1:
    if c1[0][0] == c2[0][0]:
        ans += c2[0][1]

elif c1[0][0] == c2[0][0]:
    a1 = n-c1[0][1]-c2[1][1]
    a2 = n-c1[1][1]-c2[0][1]
    ans += min(a1, a2)

else:
    ans += n//2-c1[0][1]
    ans += n//2-c2[0][1]

print(ans)
