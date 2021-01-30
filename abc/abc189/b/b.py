N, X = map(int, input().split())

X = X*100
for i in range(N):

    V, P = map(int, input().split())

    alc = V*P
    X -= alc

    if X < 0:
        print(i+1)
        exit()

print('-1')
