A, B, C = map(int, input().split())

if C > A:
    A, C = C, A

if 2*B >= C+A:
    ans = 2*B-(C+A)

else:
    ans = (((A+C) - 2*B) // 2) + ((A+C) - 2*B) % 2
print(ans)
