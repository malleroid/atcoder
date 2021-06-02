N = int(input())
s = [input() for _ in range(N)]
M = int(input())
t = [input() for _ in range(M)]

s_set = set(s)

ans = 0

for s_ in s_set:

    ans = max(ans, s.count(s_)-t.count(s_))

print(ans)
