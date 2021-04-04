import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

perm = itertools.permutations(range(1, N+1))

p_index = 0
q_index = 0
for i, ord in enumerate(perm):
    if ord == P:
        p_index = i

    if ord == Q:
        q_index = i

print(abs(q_index-p_index))
