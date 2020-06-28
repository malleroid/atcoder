n,k=map(int,input().split())

t=[int(input()) for i in range(n)]

i=2
flag=0
while i<n:

    if t[i]+t[i-1]+t[i-2]<k:

        print(i+1)
        flag+=1
        break

    i+=1

if flag==0:
    print(-1)