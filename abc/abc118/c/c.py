import math

N = int(input())
A = list(map(int, input().split()))

gcd = A[0]

for i in range(N-1):
    gcd = math.gcd(A[i+1], gcd)

print(gcd)
