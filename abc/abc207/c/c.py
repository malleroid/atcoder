import itertools

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for c in itertools.combinations(A, 2):

    c = list(c)
    c = sorted(c, key=lambda x: x[1])

    if c[0][2] > c[1][1]:
        ans += 1

    elif c[0][2] == c[1][1]:
        if c[0][0] % 2 == 1 and c[1][0] <= 2:
            ans += 1

print(ans)
