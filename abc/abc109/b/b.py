N = int(input())
W = [input() for _ in range(N)]

s = set(W)

if len(W) != len(s):
    print('No')

else:
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print('No')
            exit()

    print('Yes')
