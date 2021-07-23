x, y = map(int, input().split())

if x*y > 0:

    if y-x > 0:
        print(y-x)

    else:
        print(abs(y-x)+2)

elif x*y == 0:

    if y-x > 0:
        print(y-x)

    else:
        print(x-y+1)

else:
    print(abs(x+y)+1)
