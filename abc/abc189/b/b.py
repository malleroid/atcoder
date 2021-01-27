N,X=map(int,input().split())

for i in range(N):

    V,P=map(int,input().split())

    alc=V*P/100
    X-=alc

    if X<0:
        print(i+1)
        exit()

print('-1')