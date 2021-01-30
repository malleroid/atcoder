N=int(input())
T=[]
X=[]
Y=[]

for i in range(N):

    t,x,y=map(int,input().split())
    T.append(t)
    X.append(x)
    Y.append(y)

    if x+y>t or (x+y)%2!=t%2:
        print('No')
        exit()

    if i!=0 and T[i]-T[i-1]<abs(X[i]-X[i-1])+abs(Y[i]-Y[i-1]):
        print('No')
        exit()

print('Yes')
