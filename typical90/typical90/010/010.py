N = int(input())
cp = [[0]*N for _ in range(2)]

for i in range(N):
    C, P = map(int, input().split())
    C -= 1
    cp[C][i] = P

s = [[0]*N for _ in range(2)]
p1, p2 = 0, 0
for i in range(N):
    p1 += cp[0][i]
    p2 += cp[1][i]

    s[0][i] = p1
    s[1][i] = p2

Q = int(input())
for i in range(Q):
    L, R = map(int, input().split())
    L -= 2
    R -= 1

    s1 = s[0][R]-s[0][L] if L >= 0 else s[0][R]
    s2 = s[1][R]-s[1][L] if L >= 0 else s[1][R]

    print(s1, s2, sep=' ')
