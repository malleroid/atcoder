import math

N = int(input())
T = [int(input()) for _ in range(N)]

ans = T[0]
for i in range(N):
    num = math.gcd(ans, T[i])
    ans = ans//num*T[i]

print(ans)
