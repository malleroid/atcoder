import collections

N = int(input())
D = list(map(int, input().split()))

mod = 998244353

if D[0] != 0:
    print(0)
    exit()

c = sorted(dict(collections.Counter(D)).items())

i = 0
ans = 0
for k, v in c:
    if k == 0 and v != 1:
        print(0)
        exit()

    if k != i:
        print(0)
        exit()

    if k == 0:
        ans = 1

    else:
        ans = (ans * pow(c[i-1][1], v, mod)) % mod

    i += 1

print(ans)
