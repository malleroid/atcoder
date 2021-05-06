A, B, C, D = map(int, input().split())

t = C//B if C % B == 0 else C//B+1
a = A//D if A % D == 0 else A//D+1

print('Yes' if t <= a else 'No')
