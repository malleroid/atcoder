S = input()
alp = [False]*26

if len(S) == 26:

    for i in range(1, 26):
        if ord(S[-i]) > ord(S[-i-1]):
            T = list(S[-i:])
            s = S[-i-1]
            T.sort()

            for t in T:
                if ord(s) < ord(t):
                    s = t
                    break

            S = S[:-i-1]+s
            print(S)
            exit()

    print(-1)

else:
    for i in range(len(S)):
        alp[ord(S[i])-97] = True

    for i in range(26):
        if alp[i] is False:
            S += chr(ord('a')+i)
            break

    print(S)
