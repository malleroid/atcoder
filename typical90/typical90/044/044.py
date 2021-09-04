N, Q = map(int, input().split())
A = list(map(int, input().split()))

m = 0
for i in range(Q):
    T, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if T == 1:
        A[(x-m) % N], A[(y-m) % N] = A[(y-m) % N], A[(x-m) % N]

    elif T == 2:
        m += 1

    else:
        print(A[(x-m) % N])
