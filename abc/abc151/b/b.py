N, K, M = map(int, input().split())
A = list(map(int, input().split()))

p = M*N-sum(A)

if p <= 0:
    print(0)

elif p <= K:
    print(p)

else:
    print(-1)
