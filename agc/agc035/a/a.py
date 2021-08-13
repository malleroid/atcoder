import collections

N = int(input())
a = list(map(int, input().split()))

c = collections.Counter(a)

if len(c) == 1 and list(c.keys())[0] == 0:
    print('Yes')

elif len(c) == 2:
    key = list(c.keys())
    if 0 in key and c[0] == len(a)//3:
        print('Yes')

    else:
        print('No')

elif len(c) == 3:
    key = c.keys()
    val = c.values()

    xor = 0
    for k in key:
        xor ^= k

    s = set(val)
    if xor == 0 and len(s) == 1:
        print('Yes')

    else:
        print('No')

else:
    print('No')
