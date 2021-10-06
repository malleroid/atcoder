T, A, B, C, D = map(int, input().split())

if A+C <= T:
    print(B+D)

elif A > T and C > T:
    print(0)

else:
    a = [[A, B], [C, D]]
    a.sort(reverse=True, key=lambda x: x[1])

    if a[0][0] > T:
        print(a[1][1])

    else:
        print(a[0][1])
