import collections

N, M = map(int, input().split())
A = list(map(int, input().split()))

c = collections.Counter(A)
m = c.most_common()

print(m[0][0] if m[0][1] > N/2 else '?')
