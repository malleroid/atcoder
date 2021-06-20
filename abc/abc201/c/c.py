S = input()

o = []
x = []
q = []

for i in range(len(S)):
    if S[i] == 'o':
        o.append(str(i))
    elif S[i] == 'x':
        x.append(str(i))
    elif S[i] == '?':
        q.append(str(i))

if len(o) >= 5 or len(x) == 10:
    print(0)
    exit()

ans = 0
for i in range(10**4):

    s = str(i).zfill(4)
    fl = True

    for i in range(10):
        if S[i] == 'o' and s.count(str(i)) == 0:
            fl = False
            break
        elif S[i] == 'x' and s.count(str(i)) >= 1:
            fl = False
            break

    if fl is True:
        ans += 1

print(ans)
