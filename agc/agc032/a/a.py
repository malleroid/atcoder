N = int(input())
b = list(map(int, input().split()))

rev = [0]*N
for i in range(N):

    num = 0
    for j in range(len(b)):
        if b[j] == j+1:
            num = j+1

    if num == 0:
        print(-1)
        exit()

    else:
        b.pop(num-1)
        rev[i] = num

rev.reverse()

print(*rev, sep='\n')
