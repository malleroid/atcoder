N = int(input())
S = [input() for _ in range(N)]

ans = 10**12

for i in range(10):
    num_cnt = [0]*10

    t = 0
    for j in range(N):
        s = S[j]
        s_index = s.index(str(i))

        num_cnt[s_index] += 1
        t = max(t, s_index+10*(num_cnt[s_index]-1))

    ans = min(ans, t)

print(ans)
