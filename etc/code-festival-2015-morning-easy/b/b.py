N = int(input())
S = input()

if len(S) % 2 != 0:

    print('-1')

else:

    t = len(S)//2

    S_1 = S[:t]
    S_2 = S[t:]

    ans = 0

    for i in range(t):

        if S_1[i] != S_2[i]:
            ans += 1

    print(ans)
