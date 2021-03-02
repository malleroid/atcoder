N, T = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = 0

for i in range(N):

    ans += A[i+1]-A[i] if i+1 < N and A[i+1]-A[i] < T else T

print(ans)
