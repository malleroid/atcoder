W = int(input())

ans = [0]*(300)

for i in range(100):
    ans[i] = i+1

for i in range(100):
    ans[i+100] = (i+1)*10**2

for i in range(100):
    ans[i+200] = (i+1)*10**4

print(300)
print(*ans, sep=' ')
