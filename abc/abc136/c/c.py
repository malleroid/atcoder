N = int(input())
H = list(map(int, input().split()))

for i in range(N-1):

    if H[N-i-1] >= H[N-i-2]:
        continue

    else:
        H[N-i-2] = H[N-i-2]-1

    if H[N-i-1] < H[N-i-2]:
        print('No')
        exit()

print('Yes')
