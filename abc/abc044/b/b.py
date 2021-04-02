import collections
w = input()

c = collections.Counter(w)

for i in range(len(c)):
    if list(c.values())[i] % 2 == 1:
        print('No')
        exit()

print('Yes')
