N, S, T = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = 0
now = 0
for i in range(N):
    now += A[i]
    if S <= now <= T:
        ans += 1

print(ans)
