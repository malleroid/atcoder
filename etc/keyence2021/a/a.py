N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

max_num=0
a_max=a[0]

for i in range(N):

    a_max=max(a_max,a[i])
    
    max_num=max(max_num,b[i]*a_max)

    print(max_num)