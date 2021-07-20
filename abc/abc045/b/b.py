a = list(input())
b = list(input())
c = list(input())

d = ['a', 'b', 'c']

now = 0
while True:

    if now == 0:
        if len(a) == 0:
            print('A')
            exit()

        else:
            now = d.index(a[0])
            a.pop(0)

    elif now == 1:
        if len(b) == 0:
            print('B')
            exit()

        else:
            now = d.index(b[0])
            b.pop(0)

    elif now == 2:
        if len(c) == 0:
            print('C')
            exit()

        else:
            now = d.index(c[0])
            c.pop(0)
