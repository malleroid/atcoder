import itertools

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for a, b, c, d, e in itertools.combinations(A, 5):

    num = a % P*b % P*c % P*d % P*e % P
    if num == Q:
        ans += 1

print(ans)
