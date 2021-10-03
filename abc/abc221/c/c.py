import itertools
import copy

N = list(input())
c = len(N)//2

ans = 0
for d in itertools.combinations(N, c):
    d = list(d)
    n = copy.deepcopy(N)

    for dd in d:
        n.remove(dd)

    d.sort(reverse=True)
    n.sort(reverse=True)

    ans = max(ans, int(''.join(d))*int(''.join(n)))

print(ans)
