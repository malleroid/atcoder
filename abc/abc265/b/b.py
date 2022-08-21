N, M, T = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(M)]

hash_xy = {}
for x, y in XY:
    hash_xy[x] = y

for i in range(N-1):
    if i+1 in hash_xy:
        T += hash_xy[i+1]

    if T <= A[i]:
        print('No')
        exit()

    T -= A[i]

print('Yes')
