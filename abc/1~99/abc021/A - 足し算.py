n=int(input())

ans=0
l=0
if n%2==1:
    
    l=1
    n-=1
    ans+=1

m=n//2

ans+=m

print(ans)
if l == 1:
    print(1)

while n>=2:
    print(2)
    n-=2