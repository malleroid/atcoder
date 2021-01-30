a=int(input())
b=int(input())
c=int(input())
x=int(input())

ans=0

for i in range(a+1):

    for j in range(b+1):

        num=x-500*i-100*j

        if num >= 0 and num // 50 <= c:
            ans+=1 

print(ans)