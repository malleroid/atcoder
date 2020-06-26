n,r=map(int,input().split())

if n>=10:
    print(r)

elif n<10:
    minus = 100*(10-n)
    print(r+minus)