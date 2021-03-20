N = int(input())
v = list(map(float, input().split()))

v.sort()

for i in range(N-1):
    x = v.pop(0)
    y = v.pop(0)

    z = (x+y)/2
    v.insert(0, z)

print(*v)
