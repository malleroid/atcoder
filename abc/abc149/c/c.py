import math
X = int(input())

while True:
    sq = int(math.sqrt(X))

    prime = True
    for i in range(2, sq+1):
        if X % i == 0:
            prime = False
            break

    if prime is True:
        print(X)
        exit()

    X += 1
