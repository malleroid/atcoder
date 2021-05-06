N = int(input())
A = list(map(int, input().split()))

num = 0
for i in range(N):
    if A[i] % 2 != 0:
        num += 1

print('YES' if num % 2 == 0 else 'NO')
