N, Q = map(int, input().split())
a = list(map(int, input().split()))

d = {}

for i in range(N):
    d.setdefault(a[i], [])
    d[a[i]].append(i+1)

key = d.keys()
for i in range(Q):
    x, k = map(int, input().split())
    k -= 1
    print(d[x][k] if x in key and k < len(d[x]) else '-1')
