n=int(input())
a=list(map(int, input().split()))

i=0
num=0

if min(a)==1:
    print('1')

else:

    while i<n:

        j=0
        jud=1
        while j<n:
            if i!=j:
                if a[i]>=a[j]:

                    if a[i]%a[j]==0:
                        jud=0
                        break

            j+=1

        if jud==1:
            num+=1

        i+=1

    print(num)