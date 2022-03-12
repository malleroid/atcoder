N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
S = input()

d = {}

for i in range(N):
    d.setdefault(XY[i][1], []).append(i)

for y in d:
    target_list = d[y]
    left = pow(10, 10)
    right = 0

    if len(target_list) >= 2:
        for num in target_list:
            if S[num] == 'R':
                left = min(left, XY[num][0])
            elif S[num] == 'L':
                right = max(right, XY[num][0])

    if left < right:
        print('Yes')
        exit()

print('No')
