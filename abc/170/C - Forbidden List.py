x, n=map(int, input().split())
p=list(map(int, input().split()))

i=0

while i<200:
    
    jud=1
    con=x-i

    for j in range(n):

        if con==p[j]:
            jud=0
            break

    if jud==1:
        print(con)
        break

    jud=1
    con=x+i

    for k in range(n):

        if con==p[k]:
            jud=0
            break

    if jud==1:
        print(con)
        break

    i+=1