N, K = map(int, input().split())

for i in range(N):
    a = int(input())
    K = K-a

    if K <= 0:
        print(i+1)
        exit()
