import collections

n=int(input())
d=[int(input()) for _ in range(n)]

c=collections.Counter(d)

print(len(c))