n,m,k=map(int,input().split())

a=list(map(int, input().split()))
b=list(map(int, input().split()))

ans=0

while k>0:

    if not a:
        if not b:
            break

        else:
            k-=b.pop(0)

    else:
        if not b:
            k-=a.pop(0)

        else:        
            if a[0]<=b[0]:
                k-=a.pop(0)

            elif a[0]>b[0]:
                k-=b.pop(0)

    if k>=0:
        ans+=1

print(ans)
