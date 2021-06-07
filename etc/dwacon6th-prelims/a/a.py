N = int(input())
st = [list(input().split()) for _ in range(N)]
X = input()

p = 0
for i, v in enumerate(st):
    if st[i][0] == X:
        p = i+1
        break

ans = 0
for i in range(p, N):
    ans += int(st[i][1])

print(ans)
