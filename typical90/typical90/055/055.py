# 定数倍見積
# pythonで出してみる
import itertools

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for a, b, c, d, e in itertools.combinations(A, 5):

    if a*b % P * c % P*d % P * e % P == Q:
        ans += 1

print(ans)
