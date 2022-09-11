import math

N = int(input())
A = list(map(int, input().split()))

gcd_number = 0

for i in range(N-1):
    gcd_number = math.gcd(gcd_number, abs(A[i+1]-A[i]))

print(1 if gcd_number != 1 else 2)
