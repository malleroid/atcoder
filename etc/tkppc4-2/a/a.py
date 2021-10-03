x, y = map(int, input().split())

if y % 2 == 0:
    c = y//2
    if c >= abs(x) and c % 2 == abs(x) % 2:
        print(c)

    else:
        print(-1)

else:
    print(-1)
