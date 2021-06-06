x, y = map(int, input().split())

s = [0, 1, 2]

if x == y:
    print(s[x])

else:
    print(s[3-x-y])
