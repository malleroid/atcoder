Q = int(input())

num = []
num_cnt = []
pos = 0

for _ in range(Q):
    n, *k = map(int, input().split())

    if n == 1:
        x, c = k
        num.append(x)
        num_cnt.append(c)

    elif n == 2:
        c = k[0]
        ans = 0

        while c > 0:
            if num_cnt[pos] >= c:
                ans += num[pos]*c
                num_cnt[pos] -= c
                c = 0

            else:
                c -= num_cnt[pos]
                ans += num[pos]*num_cnt[pos]
                num_cnt[pos] = 0
                pos += 1

        print(ans)
