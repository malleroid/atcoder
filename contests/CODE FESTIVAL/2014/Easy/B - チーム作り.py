n=int(input())

if (n-1)//20%2==0:
    
    while (n-1)>=20:
        n-=20

    print(n)

else:

    while (n-1)>=20:
        n-=20

    print(20-n+1)