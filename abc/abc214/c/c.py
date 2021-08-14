N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

p = 0
num = pow(10, 10)
for i, v in enumerate(T):
    if v < num:
        num = v
        p = i

for i in range(p, p+N+1):

    if T[i % N] > T[(i-1) % N]+S[(i-1) % N]:
        T[i % N] = T[(i-1) % N]+S[(i-1) % N]

for i in range(N):
    print(T[i])
