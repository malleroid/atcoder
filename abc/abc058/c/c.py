import collections

n = int(input())
S = [input() for _ in range(n)]

c = collections.Counter(S[0])

for i in range(n-1):
    d = collections.Counter(S[i+1])

    for k, v in c.items():
        v = min(v, d[k])
        c[k] = v

ans = ''
for i in range(26):
    s = chr(ord('a')+i)
    num = c.pop(s, None)
    if num:
        ans += s*num

print(ans)
