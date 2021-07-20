import math

N, M = map(int, input().split())
S = input()
T = input()

g = math.gcd(N, M)
lcm = N//g*M
n = N//g
m = M//g
for i in range(g):

    if S[i*n] != T[i*m]:
        print(-1)
        exit()

print(lcm)
