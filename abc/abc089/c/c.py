import itertools

N = int(input())
d = {chr(ord('A')+i): 0 for i in range(26)}

for i in range(N):
    s = input()
    d[s[0]] += 1

mat = [[k, v] for k, v in d.items() if k == 'M' or k == 'A' or k ==
       'R' or k == 'C' or k == 'H']

ans = 0
for comb in itertools.combinations(mat, 3):
    ans += comb[0][1]*comb[1][1]*comb[2][1]

print(ans)
