c = list(input().split(' '))

for x in c[:]:

    if len(x) == 0:

        c.remove(x)

print(','.join(c))
