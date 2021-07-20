W, H, N = map(int, input().split())

X = [True]*W
Y = [True]*H

for i in range(N):
    x, y, a = map(int, input().split())

    if a == 1:
        for j in range(x):
            X[j] = False

    elif a == 2:
        for j in range(1, W-x+1):
            X[-j] = False

    elif a == 3:
        for j in range(y):
            Y[j] = False

    elif a == 4:
        for j in range(1, H-y+1):
            Y[-j] = False

ans = 0
c = Y.count(True)
for i in range(W):

    if X[i] is True:
        ans += c

print(ans)
