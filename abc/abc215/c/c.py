import itertools
import collections
import math
S, K = input().split()
K = int(K)

S = list(S)

c = collections.Counter(S)
num = 1
for k, v in c.items():
    num *= math.factorial(v)

a = []
for i in itertools.permutations(S):
    a.append(list(i))

a.sort()
print(''.join(a[(K-1)*num]))
