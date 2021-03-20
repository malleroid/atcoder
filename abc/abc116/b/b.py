s = int(input())

a = [s]
n = s
flag = False
while flag is False:
    if n % 2 == 0:
        n = n/2

    else:
        n = 3*n+1

    if n in a:
        flag = True

    a.append(n)

print(len(a))
