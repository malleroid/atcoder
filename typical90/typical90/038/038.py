# 最大公約数, 最小公倍数
import math

A, B = map(int, input().split())

gcd = math.gcd(A, B)

print(A//gcd*B if A//gcd*B <= pow(10, 18) else 'Large')
