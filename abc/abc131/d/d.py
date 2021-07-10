N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ab = sorted(AB, key=lambda x: x[1])

now = 0
for i in range(N):
    now += ab[i][0]

    if now > ab[i][1]:
        print('No')
        exit()

print('Yes')
