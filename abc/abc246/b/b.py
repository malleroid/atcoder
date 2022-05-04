import math

A, B = map(int, input().split())

a = A/math.sqrt(A**2+B**2)
b = B/math.sqrt(A**2+B**2)

print(a, b)
