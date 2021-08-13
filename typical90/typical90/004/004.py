H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

r_sum = [sum(r) for r in A]
c_sum = [sum(c) for c in zip(*A)]

for i in range(H):

    ans = [r_sum[i]+c_sum[j]-A[i][j] for j in range(W)]
    print(*ans)
