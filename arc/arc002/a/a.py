Y = int(input())

if Y % 4 == 0:

    if Y % 400 == 0:
        print('YES')

    elif Y % 100 == 0:
        print('NO')

    else:
        print('YES')

else:
    print('NO')
