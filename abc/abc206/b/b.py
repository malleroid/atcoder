N = int(input())

num = 0
for i in range(pow(10, 9)):

    num += i
    if num >= N:
        print(i)
        exit()
