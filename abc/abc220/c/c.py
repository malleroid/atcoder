N = int(input())
A = list(map(int, input().split()))
X = int(input())

s = sum(A)
n = X//s

cnt = X-s*n

for i in range(N):
    cnt -= A[i]
    if cnt < 0:
        p = i+1
        break

print(N*n+p)
