N, K = map(int, input().split())

ans = 0

for i in range(N):
    for j in range(K):
        n = str(i+1)+'0'+str(j+1)
        n = int(n)

        ans += n

print(ans)
