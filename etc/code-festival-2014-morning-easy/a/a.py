import statistics

n = int(input())
a = list(map(int, input().split()))

d = []

for i in range(n-1):

    d.append(a[i+1]-a[i])

print(statistics.mean(d))
