A, B = map(int, input().split())

ans = 0
for i in range(A, B+1):
    s = str(i)
    t = s[::-1]
    if s == t:
        ans += 1

print(ans)
