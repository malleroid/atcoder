N = int(input())
d = list(map(int, input().split()))

d.sort()
a = d[N//2-1]
b = d[N//2]

print(b-a)
