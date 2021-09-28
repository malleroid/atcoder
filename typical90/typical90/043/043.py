import collections

H, W = map(int, input().split())
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
S = [list(input()) for _ in range(H)]

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

q = collections.deque()

m = [(-1, 0), (1, 0), (0, -1), (0, 1)]
S[r1][c1] = 0

q.append([r1, c1, 0])

while q:
    p = q.popleft()

    for x, y in m:
        a, b, c = p[0], p[1], p[2]
        while True:
            if 0 <= a+x < H and 0 <= b+y < W and S[a+x][b+y] == '.':
                a += x
                b += y
                S[a][b] = c

                if a == r2 and b == c2:
                    print(c)
                    exit()

            else:
                q.append([a, b, c+1])
                break
