h,w=map(int,input().split())

mat=[input().split() for l in range(h)]

col=ord('A')

i=0
while i<h:

    j=0
    while j<w:
        
        if mat[i][j] == 'snuke':
            print(chr(col+j)+str(i+1))
            break

        j+=1

    i+=1

