import math

A, B, C = map(int, input().split())

gcd = math.gcd(A, B)
gcd = math.gcd(gcd, C)

print((A+B+C)//gcd-3)
