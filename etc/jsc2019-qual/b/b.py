N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9+7

last_flg = False
num = 0

for i in range(N):

    if A[i] > A[(i+1) % N]:
        num += 1

        if i == N-1:
            last_flg = True

ans = num*K % mod if last_flg is False else (num*K-1) % mod

print(ans)
