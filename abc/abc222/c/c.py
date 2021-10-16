N, M = map(int, input().split())
A = [list(input()) for _ in range(2*N)]
d = [[i, 0] for i in range(2*N)]

p = ['G', 'C', 'P']
for i in range(M):

    for j in range(N):
        left = 2*j
        right = 2*j+1
        x = p.index(A[d[left][0]][i])
        y = p.index(A[d[right][0]][i])

        judge = (x-y+3) % 3

        if judge == 1:
            d[right][1] += 1

        elif judge == 2:
            d[left][1] += 1

    d.sort(reverse=True, key=lambda x: (x[1], -x[0]))

a = [d[i][0]+1 for i in range(2*N)]

print(*a, sep='\n')
