import collections

S = input()

c = collections.Counter(S)

d = [c['a'], c['b'], c['c']]

d.sort()

print('YES' if d[2]-d[0] <= 1 else 'NO')
