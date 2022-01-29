N = int(input())
A = list(map(int, input().split()))

MOD = 10**9+7
now = 0
for i in range(N):
    now = now*10**len(str(A[i]))+A[i]
    now %= MOD

print(now)
