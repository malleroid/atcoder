H, W = map(int, input().split())
G = [list(input()) for _ in range(H)]

history = [[False]*W for _ in range(H)]

h = 0
w = 0
history[0][0] = True

while True:
    if G[h][w] == 'U':
        if h <= 0:
            print(h+1, w+1)
            exit()
        else:
            h -= 1

    elif G[h][w] == 'D':
        if h >= H-1:
            print(h+1, w+1)
            exit()
        else:
            h += 1

    elif G[h][w] == 'L':
        if w <= 0:
            print(h+1, w+1)
            exit()
        else:
            w -= 1

    elif G[h][w] == 'R':
        if w >= W-1:
            print(h+1, w+1)
            exit()
        else:
            w += 1

    if history[h][w] is True:
        print('-1')
        exit()

    else:
        history[h][w] = True
