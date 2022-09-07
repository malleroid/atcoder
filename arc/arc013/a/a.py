import itertools

N, M, L = map(int, input().split())
P, Q, R = map(int, input().split())

NML = [N, M, L]

ans = 0
for c in itertools.permutations(NML, 3):
    ans = max(ans, (c[0]//P)*(c[1]//Q)*(c[2]//R))

print(ans)
