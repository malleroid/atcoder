S = list(input())

S.append(S[0])
S.pop(0)

print(''.join(S))
