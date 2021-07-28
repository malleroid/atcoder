N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

d = {'r': P, 's': R, 'p': S}
ar = [0]*K
ans = 0
for i in range(N):

    if i < K:
        ans += d[T[i]]

    elif T[i] == T[i-K]:
        ar[i % K] += 1
        ar[i % K] %= 2

        if ar[i % K] == 0:
            ans += d[T[i]]

    else:
        ans += d[T[i]]
        ar[i % K] = 0

print(ans)
