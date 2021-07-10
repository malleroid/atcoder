import itertools

L, R = map(int, input().split())

if R-L+1 >= 2019:
    print(0)

else:
    mod = [0]*(R-L+1)
    for i in range(R-L+1):

        mod[i] = (L+i) % 2019

    ans = 2019*2
    for comb in itertools.combinations(mod, 2):
        ans = min(ans, comb[0]*comb[1] % 2019)

    print(ans)
