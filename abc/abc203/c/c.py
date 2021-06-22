N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort()

for i in range(N):
    if K-AB[i][0] < 0:
        print(K)
        exit()

    else:
        K += AB[i][1]

    if i == N-1:
        K -= AB[i][0]

print(AB[N-1][0]+K)
