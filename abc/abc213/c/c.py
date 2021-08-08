H, W, N = map(int, input().split())

AB = [0]*N
for i in range(N):
    A, B = map(int, input().split())
    arr = [A, B, i]
    AB[i] = arr

AB.sort()

cnt = 1
now = AB[0][0]
for i in range(N):

    if now == AB[i][0]:
        AB[i][0] = cnt

    else:
        now = AB[i][0]
        cnt += 1
        AB[i][0] = cnt

AB = sorted(AB, key=lambda x: x[1])

cnt = 1
now = AB[0][1]
for i in range(N):

    if now == AB[i][1]:
        AB[i][1] = cnt

    else:
        now = AB[i][1]
        cnt += 1
        AB[i][1] = cnt

AB = sorted(AB, key=lambda x: x[2])

for i in range(N):
    print(AB[i][0], AB[i][1], sep=' ')
