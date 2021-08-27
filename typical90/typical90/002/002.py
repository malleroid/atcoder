import itertools

N = int(input())

if N % 2 != 0:
    print()

else:
    for v in itertools.product(['(', ')'], repeat=N):

        num = 0
        for w in v:
            num = num+1 if w == '(' else num-1
            if num < 0:
                break

        if num == 0:
            print(''.join(v))
