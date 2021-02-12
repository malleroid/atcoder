import math

N = int(input())

num = 1
for i in range(2, N+1):

    num = num*i//math.gcd(num, i)

print(num+1)
