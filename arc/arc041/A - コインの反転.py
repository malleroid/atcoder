x,y=map(int,input().split())
k=int(input())

if y>=k:
    tail=y-k
    head=x+k

elif y<k:
    tail=k-y
    head=x+y-tail

print(head)