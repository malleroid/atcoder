Q = int(input())

m = []
for i in range(Q):
    t, x = map(int, input().split())

    if t == 1:
        m.insert(0, x)
    elif t == 2:
        m.append(x)
    else:
        print(m[x-1])
