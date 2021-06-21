S = input()

S = S[::-1]
S = S.replace('6', 't')
S = S.replace('9', '6')
S = S.replace('t', '9')

print(S)
