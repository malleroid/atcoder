X, K, D = map(int, input().split())

X = abs(X)
n = X//D

if K <= n:
    ans = X-D*K

else:
    K -= n
    X -= n*D
    ans = abs(X-D*(K % 2))

print(ans)
