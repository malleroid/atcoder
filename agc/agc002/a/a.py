a, b = map(int, input().split())

if (a < 0 and b > 0) or a == 0 or b == 0:
    print('Zero')

elif a < 0 and b < 0:
    num = a-b-1
    print('Positive' if num % 2 == 0 else 'Negative')

else:
    print('Positive')
