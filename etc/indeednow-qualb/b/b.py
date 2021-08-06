import collections

s = input()
t = input()

sc = collections.Counter(s)
tc = collections.Counter(t)

if sc != tc:
    print(-1)

else:

    for i in range(len(s)):
        p = s[:-i]
        q = s[-i:]

        if p in t and q in t:
            print(i)
            exit()

    print(-1)
