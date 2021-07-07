import math

A, B, C, D = map(int, input().split())

divC = B//C-(A-1)//C
divD = B//D-(A-1)//D

gcd = math.gcd(C, D)

lcm = C//gcd*D

divlcm = B//lcm-(A-1)//lcm

print(B-A+1-divC-divD+divlcm)
