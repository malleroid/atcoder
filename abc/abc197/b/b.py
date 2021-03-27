H, W, X, Y = map(int, input().split())
S = [list(input()) for _ in range(H)]

ans = 1
x = int(X)
while x-2 >= 0:
    if S[x-2][Y-1] == '.':
        ans += 1
    else:
        break
    x -= 1

x = int(X)
while x < H:
    if S[x][Y-1] == '.':
        ans += 1
    else:
        break
    x += 1

y = int(Y)
while y-2 >= 0:
    if S[X-1][y-2] == '.':
        ans += 1
    else:
        break
    y -= 1

y = int(Y)
while y < W:
    # print(S[X-1][Y])
    if S[X-1][y] == '.':
        ans += 1
    else:
        break
    y += 1

print(ans)
