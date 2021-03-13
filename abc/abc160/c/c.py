K, N = map(int, input().split())
A = list(map(int, input().split()))

num = 0
p = 0
for i in range(N):
    if i == N-1:
        d = A[0]+(K-A[N-1])
    else:
        d = A[i+1]-A[i]
    if num < d:
        num = d
        p = i

ans = 0
for i in range(N):
    if p == i:
        continue
    elif i == N-1:
        d = A[0]+(K-A[N-1])
    else:
        d = A[i+1]-A[i]

    ans += d

print(ans)
