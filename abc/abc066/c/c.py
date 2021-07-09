n = int(input())
a = list(map(int, input().split()))

b1 = [v for i, v in enumerate(a) if i % 2 == 0]
b2 = [v for i, v in enumerate(a) if i % 2 != 0]

if n % 2 == 0:
    b2 = b2[::-1]
    print(*(b2+b1))

else:
    b1 = b1[::-1]
    print(*(b1+b2))
