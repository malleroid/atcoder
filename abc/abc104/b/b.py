S = list(input())

if S[0] != 'A':
    print('WA')
    exit()

s = S[2:-1]

if s.count('C') != 1:
    print('WA')
    exit()

S.remove('A')
S.remove('C')

S = ''.join(S)
print('AC' if S.islower() else 'WA')
