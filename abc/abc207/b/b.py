A, B, C, D = map(int, input().split())

if B >= C*D:
    print(-1)

else:
    fl = False
    c = A
    r = 0
    num = 0
    while fl is False:

        if c <= D*r:
            print(num)
            fl = True

        else:
            c += B
            r += C
            num += 1
