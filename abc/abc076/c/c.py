S = input()
T = input()

s = len(S)
t = len(T)

for i in range(s-t+1):
    flg = True

    for j in range(t):
        if S[s-t-i+j] != '?' and S[s-t-i+j] != T[j]:
            flg = False
            break

    if flg is True:
        n = S[:-i-t]
        n = n.replace('?', 'a')
        n += T
        if len(n) < s:
            n += S[len(n):].replace('?', 'a')
        print(n)
        exit()

print('UNRESTORABLE')
