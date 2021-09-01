X = input()

ch_c = X.count('ch')
o_c = X.count('o')
k_c = X.count('k')
u_c = X.count('u')

print('YES' if ch_c*2+o_c+k_c+u_c == len(X) else 'NO')
