N,K=map(int,input().split())
a=list(map(int,input().split()))

d={}

left=0
right=0
ans=0
for i in range(N):
    d.setdefault(a[i], []).append(i)
    right=i+1
    if len(d)<=K:
        ans=max(ans,right-left)

    else:
        d[a[left]].remove(left)
        if len(d[a[left]])==0:
            d.pop(a[left])
        left+=1

print(ans)