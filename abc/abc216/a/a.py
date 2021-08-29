
X = input()

Y = int(X[-1])

if 0 <= Y <= 2:
    print(X[:-2]+'-')

elif 3 <= Y <= 6:
    print(X[:-2])

else:
    print(X[:-2]+'+')
