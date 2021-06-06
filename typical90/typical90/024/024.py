#
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_sum = sum(A)
b_sum = sum(B)

if (a_sum+K) % 2 != b_sum % 2:
    print('No')
    exit()

num = 0
for i in range(N):
    num += abs(A[i]-B[i])

print('Yes' if num <= K else 'No')
