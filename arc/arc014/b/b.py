N = int(input())
W = [input() for _ in range(N)]

s = set()
s.add(W[0])
before = W[0][-1]
for i in range(1, N):

    bef_l = len(s)
    s.add(W[i])

    if before != W[i][0] or len(s) == bef_l:
        print('WIN' if i % 2 == 1 else 'LOSE')
        exit()

    before = W[i][-1]

print('DRAW')
