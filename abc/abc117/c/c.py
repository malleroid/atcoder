N, M = map(int, input().split())
X = list(map(int, input().split()))

if N >= M:
    print(0)

else:
    X.sort()
    dif = [0]*(M-1)
    for i in range(M-1):
        dif[i] = abs(X[i+1]-X[i])

    dif.sort(reverse=True)
    mov = dif[N-1:]

    print(sum(mov))
