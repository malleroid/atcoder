n=int(input())
a=list(map(int,input().split()))

ng=1

for i in range(n):
    if a[i]%2==0:
        ng*=2

print(3**n-ng)