import itertools

N, M = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int, input().split()))

for v in itertools.product([False, True], repeat=N):

    for i in range(M):
