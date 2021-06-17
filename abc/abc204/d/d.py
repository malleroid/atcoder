N = int(input())
T = list(map(int, input().split()))

s = sum(T)

t1 = 0
t2 = 0

for i in range(N):

    if t1 >= t2:
        t2 += T[i]

    else:
        t1 += T[i]

print(max(t1, t2))
