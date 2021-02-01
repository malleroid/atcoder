S = input()
t = list('AKIHABARA')

if len(S) > len(t) or 'AA' in S:
    print('NO')

else:
    a = len(t)-len(S)
    S = list(S)
    for i in range(len(t)):

        if i >= len(S) or t[i] != S[i]:

            S.insert(i, 'A')
            a -= 1

        if a < 0:
            print('NO')
            exit()

    print('YES' if S == t else 'NO')
