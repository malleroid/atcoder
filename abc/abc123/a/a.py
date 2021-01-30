p=[int(input()) for _ in range(5)]
k=int(input())

p.sort()
print('Yay!' if p[-1]-p[0]<=k else ':(')