import collections
N = int(input())
S = [input() for _ in range(N)]

c = collections.Counter(S)

m = c.most_common()
k = m[0][1]

ans = []
for i in range(len(m)):
    if m[i][1] == k:
        ans.append(m[i][0])

    else:
        break

ans.sort()
print('\n'.join(ans))
