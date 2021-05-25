import itertools

A = list(map(int, input().split()))
n = len(A)

for bits in itertools.product([0, 1], repeat=n):
    a = [x for bit, x in zip(bits, A) if bit == 1]

    if sum(a) == sum(A)/2:
        print('Yes')
        exit()

print('No')
