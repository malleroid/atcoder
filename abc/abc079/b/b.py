N = int(input())

L = [2, 1]

if N == 1:
    print(L[1])

else:
    for i in range(2, N+1):
        L.append(L[i-1]+L[i-2])

    print(L[-1])
