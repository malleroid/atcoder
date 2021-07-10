N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if i % 2 == 1:
        A[i] -= 1

print('Yes' if sum(A) <= X else 'No')
