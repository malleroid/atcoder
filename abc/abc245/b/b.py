N = int(input())
A = list(map(int, input().split()))

c = [True]*(2001)

for i in range(N):
    c[A[i]] = False

for i in range(2001):
    if c[i]:
        print(i)
        exit()
