A, B = map(int, input().split())

r = 10**4

for i in range(1, r+1):
    if i*8//100 == A and i*10//100 == B:
        print(i)
        exit()

print(-1)
