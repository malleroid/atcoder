N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

A, B = [list(i) for i in zip(*AB)]
a_sum = sum(A)
b_sum = sum(B)

d = [0]*N
for i in range(N):
    d[i] = A[i]-B[i]

d.sort(reverse=True)

if a_sum <= T:
    print(0)
    exit()

else:
    now = a_sum
    for i in range(N):
        now -= d[i]
        if now <= T:
            print(i+1)
            exit()

    print(-1)
