N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]

INF = pow(10, 15)

warshallfloyd = [[INF]*N for _ in range(N)]

for i in range(N):

    warshallfloyd[i][i] = 0

for i in range(M):
    warshallfloyd[ABC[i][0]-1][ABC[i][1]-1] = ABC[i][2]

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            warshallfloyd[i][j] = min(
                warshallfloyd[i][j], warshallfloyd[i][k]+warshallfloyd[k][j])

            if warshallfloyd[i][j] < INF:
                ans += warshallfloyd[i][j]

print(ans)
