H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]

for i in range(H):

    for j in range(W):

        if s[i][j] == '#':

            if (i != 0 and s[i-1][j] == '.') and (j != 0 and s[i][j-1] == '.') and (i != H-1 and s[i+1][j] == '.') and (j != W-1 and s[i][j+1] == '.'):

                print('No')
                exit()

print('Yes')
