N = int(input())

for i in range(N//4+1):

    for j in range(N//7+1):

        if N == 4*i+7*j:
            print('Yes')
            exit()

print('No')
