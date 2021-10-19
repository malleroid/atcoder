N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(M)]

cnt = N-M+1

for i in range(cnt):
    for j in range(cnt):

        r_flg = True
        for p in range(M):
            for q in range(M):
                if B[p][q] != A[p+i][q+j]:
                    r_flg = False
                    break

            if r_flg is False:
                break

        if r_flg:
            print('Yes')
            exit()

print('No')
