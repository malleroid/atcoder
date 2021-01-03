a,b,c=map(int,input().split())

ans=0
while c>0:
    
    if a>=b:
        c-=b
    
    else:
        c-=a

    if c>=0:
        ans+=1

print(ans)