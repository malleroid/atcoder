N,C=map(int,input().split())
abc=[map(int,input().split()) for _ in range(N)]
a,b,c=[list(i) for i in zip(*abc)]

start_day=min(a)
last_day=max(b)
ans=0

for i in range(start_day,last_day+1):

    day_cost=0

    for j in range(N):

        if a[j]<=i<=b[j]:
            day_cost+=c[j]

    if day_cost<=C:
        ans+=day_cost

    else:
        ans+=C

print(ans)