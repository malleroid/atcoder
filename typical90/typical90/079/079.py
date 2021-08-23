H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

ans = 0
for i in range(H-1):

    for j in range(W-1):

        dif = B[i][j]-A[i][j]
        ans += abs(dif)
        A[i][j] += dif
        A[i+1][j] += dif
        A[i][j+1] += dif
        A[i+1][j+1] += dif

        if j == W-2 and B[i][j+1] != A[i][j+1]:
            print('No')
            exit()

        if i == H-2 and B[i+1][j] != A[i+1][j]:
            print('No')
            exit()

        if i == H-2 and j == W-2 and B[i+1][j+1] != A[i+1][j+1]:
            print('No')
            exit()

print('Yes')
print(ans)
