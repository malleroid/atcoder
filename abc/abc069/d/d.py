H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))

c = [[""]*W for _ in range(H)]

current_num = 1
for i in range(H):
    for j in range(W):
        if i % 2 == 0:
            c[i][j] = current_num
            a[current_num-1] -= 1
            if a[current_num-1] == 0:
                current_num += 1

        else:
            c[i][W-j-1] = current_num
            a[current_num-1] -= 1
            if a[current_num-1] == 0:
                current_num += 1

for i in range(H):
    print(*c[i])
