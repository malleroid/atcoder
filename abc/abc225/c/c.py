N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

now = B[0][0]
for i in range(N):
    r = (now-1)//7
    for j in range(M):
        if B[i][j] != now+j:
            print('No')
            exit()
        if (B[i][j]-1)//7 != r:
            print('No')
            exit()
    now += 7

print('Yes')
