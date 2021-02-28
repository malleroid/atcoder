N = int(input())

ans = 10**9

for i in range(N):

    A, P, X = map(int, input().split())

    if A >= X:
        continue

    else:
        ans = min(ans, P)

print(ans if ans != 10**9 else '-1')
