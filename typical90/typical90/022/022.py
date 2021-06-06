# 最大公約数(本来はユークリッドの互除法)
import math

A, B, C = map(int, input().split())

gcd_ab = math.gcd(A, B)
gcd = math.gcd(gcd_ab, C)

ans = A//gcd+B//gcd+C//gcd-3

print(ans)
