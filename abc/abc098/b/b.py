N=int(input())
S=input()

ans=0

for i in range(1,N):

    X=set(S[:i])
    Y=set(S[i:])

    cnt=X & Y
    ans=max(ans,len(cnt))

print(ans)