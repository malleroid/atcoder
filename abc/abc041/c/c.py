N = int(input())
a = list(map(int, input().split()))

b = []
for i in range(N):
    c = [a[i], i+1]
    b.append(c)

b.sort(reverse=True)

c = [h[1] for h in b]

print(*c, sep='\n')
