c = [list(map(int, input().split())) for _ in range(3)]

for i in range(101):
    b1 = c[0][0]-i
    b2 = c[0][1]-i
    b3 = c[0][2]-i

    if b1 < 0 or b2 < 0 or b3 < 0:
        break

    for j in range(101):
        if j+b1 != c[1][0] or j+b2 != c[1][1] or j+b3 != c[1][2]:
            continue

        for k in range(101):
            if k+b1 != c[2][0] or k+b2 != c[2][1] or k+b3 != c[2][2]:
                continue

            else:
                print('Yes')
                exit()

print('No')
