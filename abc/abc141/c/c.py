import collections

N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

n = [K-Q for _ in range(N)]

c = collections.Counter(A)

d = list(c.items())

for i in d:
    n[i[0]-1] = n[i[0]-1]+i[1]

for j in n:
    print('Yes' if j > 0 else 'No')
