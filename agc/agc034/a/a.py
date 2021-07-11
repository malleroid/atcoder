N, A, B, C, D = map(int, input().split())
S = input()

if C < D:
    a = S[A:D]

    if '##' not in a:
        print('Yes')

    else:
        print('No')

else:
    a = S[A:C]
    b = S[B-2:D+1]

    if '##' not in a and '...' in b:
        print('Yes')

    else:
        print('No')
