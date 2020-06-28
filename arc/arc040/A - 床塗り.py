n=int(input())

mat=[input() for i in range(n)]

r=0
b=0
p=0
while p<n:

    s=mat[p]
    q=0
    while q<n:
        
        if s[q]=='R':
            r+=1

        elif s[q]=='B':
            b+=1

        q+=1

    p+=1

if r>b:
    print('TAKAHASHI')

elif r<b:
    print('AOKI')

elif r==b:
    print('DRAW')