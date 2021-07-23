import math

N = int(input())
P = [int(input()) for _ in range(5)]

min_P = min(P)
ans = math.ceil(N/min_P)+4

print(ans)
