import itertools

N, W = map(int, input().split())
A = list(map(int, input().split()))

ans_s = set()

for i in range(N):
    if A[i] <= W:
        ans_s.add(A[i])

for comb in itertools.combinations(A, 2):
    if sum(comb) <= W:
        ans_s.add(sum(comb))

for triple in itertools.combinations(A, 3):
    if sum(triple) <= W:
        ans_s.add(sum(triple))

print(len(ans_s))
