N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

d = {'r': P, 's': R, 'p': S}

ans = 0
for i in range(N):
    if i < K or T[i] != T[i-K]:
        ans += d[T[i]]

    elif 2*i < K and
    print(ans)

print(ans)
