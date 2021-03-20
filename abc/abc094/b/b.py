N, M, X = map(int, input().split())
A = list(map(int, input().split()))

pos = 0
neg = 0
for i in range(N-X):
    if X+i+1 in A:
        pos += 1

for i in range(X):
    if i+1 in A:
        neg += 1

print(min(pos, neg))
