import itertools

N, K = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0
for bits in itertools.product([0, 1], repeat=N):
    cnt = [0]*26
    for i in range(N):
        if bits[i] == 1:
            for s in S[i]:
                cnt[ord(s)-ord('a')] += 1

    num = cnt.count(K)

    ans = max(ans, num)

print(ans)
