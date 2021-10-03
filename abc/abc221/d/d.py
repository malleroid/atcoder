N = int(input())

d = {}

for i in range(N):
    A, B = map(int, input().split())

    d.setdefault(A, 0)
    d.setdefault(A+B, 0)
    d[A] += 1
    d[A+B] -= 1

keys = list(d.keys())
keys.sort()

now = 0
bef = 0
k = [0]*(N+1)
for key in keys:
    k[now] += key-bef
    now += d[key]
    bef = key

print(*k[1:])
