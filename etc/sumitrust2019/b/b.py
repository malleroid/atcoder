import math

N = int(input())

ans = math.ceil(N/1.08)

print(ans if int(math.floor(ans*1.08)) == N else ':(')
