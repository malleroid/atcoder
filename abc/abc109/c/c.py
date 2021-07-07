import math

N, X = map(int, input().split())
x = list(map(int, input().split()))

for i in range(N):
    x[i] = abs(x[i]-X)

ans = x[0]
for i in range(N-1):
    ans = math.gcd(x[i+1], ans)

print(ans)
