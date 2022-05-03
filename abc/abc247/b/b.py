N = int(input())
st = [list(input().split()) for _ in range(N)]

d = {}
for i in range(N):
    s, t = st[i]

    d.setdefault(s, []).append(i)
    if s != t:
        d.setdefault(t, []).append(i)

for s, t in st:
    if len(d[s]) >= 2 and len(d[t]) >= 2:
        print("No")
        exit()

print("Yes")
