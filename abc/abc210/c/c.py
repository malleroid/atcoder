N, K = map(int, input().split())
c = list(map(int, input().split()))

cn = {}
ans = 0
for i in range(K):
    if c[i] not in cn:
        cn[c[i]] = 1
        ans += 1

    else:
        cn[c[i]] += 1

num = ans
for i in range(N-K):

    if c[K+i] not in cn:
        cn[c[K+i]] = 1
        num += 1

    else:
        cn[c[K+i]] += 1
        if cn[c[K+i]] == 1:
            num += 1

    cn[c[i]] -= 1
    if cn[c[i]] == 0:
        num -= 1

    ans = max(ans, num)

print(ans)
