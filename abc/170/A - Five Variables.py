x=list(map(int,input().split()))

i=1
while i<=len(x):
    
    if x[i-1]==0:
        print(i)
    
    i+=1