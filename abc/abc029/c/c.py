import itertools

N = int(input())

a = ['a', 'b', 'c']
for v in itertools.product(a, repeat=N):
    print(*v, sep='')
