N = int(input())
S = list(input())

s = S.count('E')

ans = s

for i in range(N):

    if S[i] == 'W':
        s += 1
        ans = min(ans, s)

    else:
        s -= 1
        ans = min(ans, s)

print(ans)
