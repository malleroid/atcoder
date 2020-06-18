x, y=map(int, input().split())

i=0
while i<=x:
    leg=i*4+(x-i)*2

    if(leg==y):
        print('Yes')
        break
    i+=1

if i>x:
    print('No')