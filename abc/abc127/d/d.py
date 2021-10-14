import collections

N, M = map(int, input().split())
A = list(map(int, input().split()))

c = collections.Counter(A)

for i in range(M):
    B, C = map(int, input().split())

    c.setdefault(C, 0)
    c[C] += B

d = sorted(c.items(), reverse=True)

ans = 0
i = 0
while N > 0:
    t = d[i]
    if t[1] > N:
        ans += t[0]*N
        N = 0
    else:
        ans += t[0]*t[1]
        N -= t[1]

    i += 1
print(ans)
