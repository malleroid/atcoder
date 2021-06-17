N = int(input())
A, B, C = map(int, input().split())

ans = 9999
for i in range(10000):
    for j in range(10000-i):

        if (N-A*i-B*j) % C == 0 and (N-A*i-B*j) // C >= 0:
            ans = min(ans, i+j+((N-A*i-B*j)//C))

print(ans)
