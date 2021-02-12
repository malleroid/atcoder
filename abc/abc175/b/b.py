import itertools

N = int(input())
L = list(map(int, input().split()))

ans = 0

for i in itertools.combinations(L, 3):

    i = sorted(i)
    if len(set(i)) == 3 and i[2] < i[0]+i[1]:
        ans += 1

print(ans)
