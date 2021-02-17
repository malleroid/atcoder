A, B = map(int, input().split())

if B == 1:
    print(0)
    exit()

i = 1
while A+(A-1)*(i-1) < B:
    i += 1

print(i)
