n=int(input())

primeflag=0
i=2

if n==1:
    print('NO')

else:
    while i<n:
        
        if n%i==0:
            primeflag+=1
            break

        i+=1

    if primeflag==0:
        print('YES')

    else:
        print('NO')