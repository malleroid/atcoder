s=input()
t=input()

i=0
ans=0

while i<len(s):

    if s[i]!=t[i]:
        ans+=1

    i+=1

print(ans)