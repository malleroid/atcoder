a=[100, 100, 200]

i=3
while i<20:

    ans=sum(a[i-3:i])
    a.append(ans)
    i+=1

print(a[19])