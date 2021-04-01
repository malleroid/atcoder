N = int(input())
A = list(map(int, input().split()))

ans = 0
while True:
    for i in range(N):
        if bin(A[i])[-1] == '1':
            print(ans)
            exit()

        else:
            A[i] = A[i] >> 1

    ans += 1
