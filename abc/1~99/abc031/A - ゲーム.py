a,d=map(int,input().split())

if (a+1)*d>=a*(d+1):
    print(str((a+1)*d))

elif (a+1)*d<a*(d+1):
    print(str(a*(d+1)))