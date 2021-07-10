N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

c = [0]*N
for i in range(M):
    if ab[i][0] == 1:
        c[ab[i][1]] = 1

for i in range(M):
    if ab[i][1] == N and c[ab[i][0]] == 1:
        print('POSSIBLE')
        exit()

print('IMPOSSIBLE')
