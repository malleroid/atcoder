a, b = map(int, input().split())

num = b-a

s = [i+1 for i in range(num-1)]

print(sum(s)-a)
