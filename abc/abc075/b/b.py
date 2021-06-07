H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

h = [-1, -1, 0, 1, 1, 1, 0, -1]
w = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(H):

    for j in range(W):
        cnt = 0
        if S[i][j] != '#':
            for k in range(8):
                if 0 <= i+h[k] < H and 0 <= j+w[k] < W:
                    if S[i+h[k]][j+w[k]] == '#':
                        cnt += 1

            S[i][j] = str(cnt)

    print(''.join(S[i]))
