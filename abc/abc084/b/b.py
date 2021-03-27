A, B = map(int, input().split())
S = input()

if S.count('-') != 1:
    print('No')

else:
    s1, s2 = S.split('-')

    print('Yes' if len(s1) == A and len(s2) == B else 'No')
