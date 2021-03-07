import math

a, b = input().split()
c = int(a+b)

print('Yes' if math.sqrt(c).is_integer() else 'No')
