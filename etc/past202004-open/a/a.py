S, T = input().split()

S = S.replace('B', '-')
S = S.replace('F', '')

T = T.replace('B', '-')
T = T.replace('F', '')

s = int(S) if int(S) > 0 else int(S)+1
t = int(T) if int(T) > 0 else int(T)+1


print(abs(s-t))
