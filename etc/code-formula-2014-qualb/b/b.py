N = list(input())
N.reverse()

even, odd = 0, 0

for i in range(len(N)):
    if i % 2 == 0:
        odd += int(N[i])

    else:
        even += int(N[i])

print(even, odd)
