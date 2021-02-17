N, A, B = map(int, input().split())
S = input()

a = 0
b = 0

for i in range(len(S)):

    s = S[i]

    if s == 'a' and A+B > a:
        print('Yes')
        a += 1

    elif s == 'b' and A+B > a and B > b:
        print('Yes')
        a += 1
        b += 1

    else:
        print('No')
