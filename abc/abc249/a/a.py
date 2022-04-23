A, B, C, D, E, F, X = map(int, input().split())

t_mod = X % (A+C)
a_mod = X % (D+F)

t_l = B*A*(X//(A+C))
a_l = E*D*(X//(D+F))

t_l += B*t_mod if t_mod <= A else B*A
a_l += E*a_mod if a_mod <= D else E*D

print('Takahashi' if t_l > a_l else 'Aoki' if t_l < a_l else 'Draw')
