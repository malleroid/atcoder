N = int(input())

T = []
for i in range(N):
    S, P = input().split()
    P = int(P)
    t = [S, P, i+1]
    T.append(t)

u = sorted(T, key=lambda t: t[1], reverse=True)
v = sorted(u, key=lambda t: t[0])

for i in range(N):
    print(v[i][2])
