import bisect

N = int(input())
A = list(map(int, input().split()))

s = sum(A)

if s % 10 != 0:
    print('No')
    exit()

else:
    num = s//10
    A *= 2

    b = [0]*(2*N+1)

    for i in range(1, 2*N+1):
        b[i] += b[i-1]+A[i-1]

    for i in range(N):
        k = b[i]+num

        p = bisect.bisect_left(b, k)

        if k == b[p]:
            print('Yes')
            exit()

    print('No')
