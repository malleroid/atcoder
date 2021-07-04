N, A, B = map(int, input().split())

if A > B:
    print(0)

elif N == 1:
    if A != B:
        print(0)

    else:
        print(1)

else:
    n_min = A*(N-1)+B
    n_max = A+B*(N-1)

    print(n_max-n_min+1)
