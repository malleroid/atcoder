import collections

N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)

print('YES' if c.most_common()[0][1] == 1 else 'NO')
