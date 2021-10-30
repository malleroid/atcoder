import itertools

N = int(input())
A = list(map(int, input().split()))

d = {}

for i in range(N):
    d.setdefault(A[i], 0)
    d[A[i]] += 1

ans = 0
for i, j in itertools.combinations(d, 2):
    ans += (i-j)**2*d[i]*d[j]

print(ans)
