import collections

S = list(input())

c = collections.Counter(S)

if len(c) == 1:
    print(1)
elif len(c) == 2:
    print(3)

else:
    print(6)
