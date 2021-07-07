s = list(input())
t = list(input())

s.sort()
t.sort(reverse=True)

sl = len(s)
tl = len(t)

leng = min(sl, tl)

for i in range(leng):

    if ord(s[i]) < ord(t[i]):
        print('Yes')
        exit()

    elif ord(s[i]) == ord(t[i]):
        continue

    else:
        print('No')
        exit()

print('Yes' if sl < tl else 'No')
