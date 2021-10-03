S = list(input())
T = list(input())

if S == T:
    print('Yes')

else:

    for i in range(len(S)-1):
        if S[i] != T[i]:
            S[i], S[i+1] = S[i+1], S[i]
            break

    print('Yes' if S == T else 'No')
