N = int(input())
A = list(map(int, input().split()))

if 0 in A:
    print(0)

else:
    ans = 1
    for i in range(N):
        ans *= A[i]

        if ans > pow(10, 18):
            print(-1)
            exit()

    print(ans)
