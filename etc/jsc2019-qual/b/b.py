N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9+7

a = [0]*N
inversion = [0]*N

for i in range(N):

    for j in range(N):

        if A[i] > A[j]:
            a[i] += 1

            if i < j:
                inversion[i] += 1

ans = 0
for i in range(N):
    ans += a[i]*K*(K-1)//2+inversion[i]*K
    ans %= mod

print(ans)
