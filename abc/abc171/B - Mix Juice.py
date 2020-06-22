n, k=map(int, input().split())
p=list(map(int, input().split()))

p.sort()

i=0
price=0
while i<k:
    price+=p[i]

    i+=1
    
print(price)