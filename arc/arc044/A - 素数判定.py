n=int(input())

if n==2 or n==3 or n==5:
    
    print('Prime')

elif n==1 or n%2==0 or n%5==0 or sum(list(map(int,str(n))))%3==0:

    print('Not Prime')

else:
    print('Prime')