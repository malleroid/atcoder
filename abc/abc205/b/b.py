N = int(input())
A = list(map(int, input().split()))

s = set(A)

print('Yes' if len(A) == len(s) else 'No')
