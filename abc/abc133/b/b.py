import itertools
import math

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i, j in itertools.combinations(X, 2):
    num = 0
    for k in range(D):
        num += (i[k]-j[k])**2

    num = math.sqrt(num)

    if num.is_integer() is True:
        ans += 1

print(ans)
