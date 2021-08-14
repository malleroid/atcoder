import math
a, b, x = map(int, input().split())

x = x/a

if x >= a*b/2:

    ans = math.atan2(2*(a*b-x), a**2)

else:

    ans = math.atan2(b**2, 2*x)

print(math.degrees(ans))
