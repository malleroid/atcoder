n,a,b=map(int,input().split())

ans=0

for i in range(1,n+1):
    
    num=0

    for j in range(len(str(i))):

        num+=int(str(i)[j])

    if a<=num<=b:
        ans+=i

print(ans) 