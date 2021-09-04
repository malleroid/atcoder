N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

P = [0]*2*N

for i in range(N):
    P[i] = AB[i][1]
    P[N+i] = AB[i][0]-AB[i][1]

P.sort(reverse=True)

Q = P[:K]

print(sum(Q))
