N, M = map(int, input().split())
A = list(map(int, input().split()))

p = [i for i in range(M+1)]

divisor = set()

for i in range(N):
    n = A[i]
    if n != 1:
        num = 1
        while num**2 <= n:
            if n % num == 0:
                divisor.add(num)
                divisor.add(n//num)
            num += 1

divisor = list(divisor)
divisor.sort()
divisor = divisor[1:]

for i in range(len(divisor)):
    n = divisor[i]
    while n <= M:
        p[n] = 0
        n += divisor[i]

ans = [i for i in p if i != 0]
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
