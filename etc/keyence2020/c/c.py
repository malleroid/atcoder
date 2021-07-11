N, K, S = map(int, input().split())

ans = [0]*N
p = pow(10, 9)
for i in range(N):

    if i < K:
        ans[i] = S

    else:
        ans[i] = (S+1) % p

print(*ans)
