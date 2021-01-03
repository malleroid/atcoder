a, r, n = map(int, input().split())

if(r==1):
    print(a)

elif(r>=2 and r<10):
    if(n>=31):
        print('large')

    else:
        res=a*r**(n-1)

        if res<=10**9:
            print(res)

        else:
            print('large')

elif(r>=10):
    if(n>=10):
        print('large')

    else:
        res=a*r**(n-1)

        if res<=10**9:
            print(res)

        else:
            print('large')