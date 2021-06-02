import itertools
import math

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

dis = 0
for p in itertools.permutations(xy, N):

    for i in range(N-1):

        dis += math.sqrt((p[i+1][0]-p[i][0])**2+(p[i+1][1]-p[i][1])**2)

print(dis/math.factorial(N))
