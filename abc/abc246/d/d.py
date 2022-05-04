N = int(input())

a = pow(10, 6)
b = pow(10, 6)
ans = pow(10, 18)


def f(a, b):
    return (a+b)*(a**2+b**2)


for i in range(a+1):
    while b > 0 and f(i, b-1) >= N:
        b -= 1

    ans = min(ans, f(i, b))

print(ans)
