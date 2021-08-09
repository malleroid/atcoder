N = int(input())

num = 1
while True:

    m = num*(num+1)//2

    if m >= N:
        break

    num += 1

except_num = m-N

for i in range(1, num+1):

    if i == except_num:
        pass
    else:
        print(i)
