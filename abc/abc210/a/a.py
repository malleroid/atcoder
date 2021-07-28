N, A, X, Y = map(int, input().split())

print(N*X if N <= A else A*X+(N-A)*Y)
