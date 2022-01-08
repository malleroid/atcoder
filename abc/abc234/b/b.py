import itertools
import math

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for i, j in itertools.combinations(xy, 2):
    num = math.sqrt((j[0]-i[0])**2+(j[1]-i[1])**2)
    ans = max(ans, num)
print(ans)
