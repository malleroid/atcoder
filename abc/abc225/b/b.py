N = int(input())

s = set()
for i in range(N-1):
    a, b = map(int, input().split())
    if len(s) == 0:
        s.add(a)
        s.add(b)

    else:
        if a not in s and b not in s:
            print('No')
            exit()

        else:
            if a in s:
                s.clear()
                s.add(a)

            elif b in s:
                s.clear()
                s.add(b)

print('Yes')
