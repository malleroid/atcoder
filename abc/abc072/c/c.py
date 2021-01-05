import collections

n=int(input())
a=list(map(int,input().split()))

dict={}

for i in range(n):
    for j in range(-1, 2):
        
        num=a[i]+j

        if num in dict:
            dict[num]+=1

        else:
            dict[num]=1

c=collections.Counter(dict)

print(c.most_common()[0][1])