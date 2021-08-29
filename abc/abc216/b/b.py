import itertools
N = int(input())
ST = [list(input().split()) for _ in range(N)]

for p, q in itertools.combinations(ST, 2):

    if p[0] == q[0] and p[1] == q[1]:
        print('Yes')
        exit()

print('No')
