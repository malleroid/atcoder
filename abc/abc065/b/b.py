N = int(input())
a = [int(input()) for _ in range(N)]

if 2 not in a:
    print('-1')

else:
    b = a[0]
    ans = 1
    for i in range(N):

        if b == 2:
            print(ans)
            exit()

        b = a[b-1]
        ans += 1

    print('-1')
