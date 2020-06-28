n=int(input())

num=0

i=0
while i<=n:
    num+=i
    i+=1

primeflag=0
j=2

if num==1:
    print('BOWWOW')

else:
    while j<num:
        
        if num%j==0:
            primeflag+=1
            break

        j+=1

    if primeflag==0:
        print('WANWAN')

    else:
        print('BOWWOW')