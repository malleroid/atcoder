N, M, C = map(int, input().split())
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    A = list(map(int, input().split()))
    num = 0

    for j in range(M):
        num += A[j]*B[j]

    if num+C > 0:
        ans += 1

print(ans)
