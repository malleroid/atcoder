n,m = map(int, input().split())

mat = [map(int, input().split()) for _ in range(m)]

a, b = [list(num) for num in zip(*mat)]

for i in range(n-1):
    now = i+1

    for j in range(n):
        