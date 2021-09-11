P = list(map(int, input().split()))

ans = [0]*26
for i in range(26):
    ans[i] = chr(ord('a')+(P[i]-1))

print(*ans, sep='')
