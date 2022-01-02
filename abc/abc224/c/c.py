import itertools

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for i, j, k in itertools.combinations(XY, 3):

    num = (i[0]*j[1]+j[0]*k[1]+k[0]*i[1]-i[1]*j[0]-j[1]*k[0]-k[1]*i[0])/2

    if num != 0:
        ans += 1

print(ans)
