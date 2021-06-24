N = int(input())
s = [int(input()) for _ in range(N)]

s.sort()

num = sum(s)

if num % 10 != 0:
    print(num)

else:
    for i in range(N):
        if s[i] % 10 != 0:
            num -= s[i]
            print(num)
            exit()

    print(0)
