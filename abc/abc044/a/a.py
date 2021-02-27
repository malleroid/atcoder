N = int(input())
K = int(input())
X = int(input())
Y = int(input())

print(X*K+Y*(N-K) if N > K else X*N)
