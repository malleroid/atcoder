N, K = map(int, input().split())

if N % K == 0:
    print(0)

elif N <= K:
    print(N if abs(N-K) >= N else abs(N-K))

else:
    d = len(str(N))-len(str(K))

    while d > 0:
        N = N-K*10**(d-1)
        d = len(str(N))-len(str(K))

    while N >= K:
        N = N-K

    print(N if abs(N-K) >= N else abs(N-K))
