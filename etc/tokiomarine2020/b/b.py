a, v=map(int,input().split())
b, w=map(int,input().split())
t=int(input())

i=0
pos_a=[a]
pos_b=[b]

while i<=t:
    j=0
    while j<=i:

        mov_a=[pos_a[j]+v,pos_a[j]-v]
        print(mov_a)
        j+=1
    pos_a.append(mov_a)

    mov_b=[b+w,b-w]
    pos_b.append(mov_b)    
    
    i+=1

print(pos_a)