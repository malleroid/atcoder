import collections

N = int(input())
r = input()

c = collections.Counter(r)

s = 0

for i, j in c.items():

    if i == 'A':

        s += 4*j

    elif i == 'B':

        s += 3*j

    elif i == 'C':

        s += 2*j

    elif i == 'D':

        s += 1*j

print(s/N)
