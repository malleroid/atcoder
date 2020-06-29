a,b,c=map(int,input().split())

i=1

while i<=127:

    if i%3==a and i%5==b and i%7==c:
        print(i)

    i+=1

