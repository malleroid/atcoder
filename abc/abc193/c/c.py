import math

N = int(input())

s = set()

for i in range(2, int(math.sqrt(N))+1):

    x = i*i

    while x <= N:
        s.add(x)
        x *= i

print(N-len(s))
