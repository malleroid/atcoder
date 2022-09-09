import collections
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())

ab = [a1, b1, a2, b2, a3, b3]

c = collections.Counter(ab)
cm = c.most_common()
print('YES' if cm[0][1] != 3 else 'NO')
