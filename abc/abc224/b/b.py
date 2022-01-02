H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

for i in range(H-1):

    for j in range(i+1, H):

        for k in range(W-1):

            for p in range(k+1, W):

                if A[i][k]+A[j][p] <= A[j][k]+A[i][p]:
                    continue

                else:
                    print('No')
                    exit()

print('Yes')
