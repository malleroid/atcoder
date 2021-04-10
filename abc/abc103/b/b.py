import collections

S = input()
T = input()

c1 = collections.Counter(S)
c2 = collections.Counter(T)

if c1 != c2:
    print('No')

else:
    for i in range(len(S)):
        S = S[-1]+S[0:-1]
        if S == T:
            print('Yes')
            exit()

    print('No')
