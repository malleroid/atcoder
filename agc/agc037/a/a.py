S = input()

ans = 0
before = ''
now = ''
for i in range(len(S)):
    s = now+S[i]
    if s != before:
        ans += 1
        before = s
        now = ''
    else:
        now += S[i]

print(ans)
