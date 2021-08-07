N, K = map(int, input().split())

dict = {}

for _ in range(N):

    a, b = map(int, input().split())

    if a in dict.keys():
        dict[a] += b

    else:
        dict[a] = b

dict = sorted(dict.items())

for k, v in dict:

    K -= v

    if K <= 0:
        print(k)
        exit()
