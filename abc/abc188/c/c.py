n = int(input())
a = list(map(int, input().split()))

half = 2**(n-1)

a1 = a[:half]
a2 = a[half:]

a1_max = max(a1)
a2_max = max(a2)

if a1_max > a2_max:
    print(a.index(a2_max)+1)

else:
    print(a.index(a1_max)+1)
