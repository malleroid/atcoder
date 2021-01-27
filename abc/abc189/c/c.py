N=int(input())
A=list(map(int,input().split()))

ans=0
cnt=0

for i in range(len(A)):

    if A[i]>=i:
        orange=A[i]-i
        eat+=orange

    else:
        ans=max(eat,ans)
        eat=0

ans=max(eat,ans)

print(ans)