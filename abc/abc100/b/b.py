d,n = map(int,input().split())

if n%100==0:
    print(100**d*(n+1))

else:
    print(100**d*n)