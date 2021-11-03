N = int(input())
s = [list(input())[::-1] for _ in range(N)]

s.sort()

for i in range(N):
    print(*s[i][::-1], sep='')
