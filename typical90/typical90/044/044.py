# 見かけ上の変化, 配列を変更しないまま扱う
N, Q = map(int, input().split())
A = list(map(int, input().split()))

m = 0
for i in range(Q):
    T, x, y = map(int, input().split())

    if T == 1:
        t = A[(x-1-m) % N]
        A[(x-1-m) % N] = A[(y-1-m) % N]
        A[(y-1-m) % N] = t

    elif T == 2:
        m += 1

    else:
        print(A[(x-1-m) % N])
