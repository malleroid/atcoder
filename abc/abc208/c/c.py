import bisect

N, K = map(int, input().split())
a = list(map(int, input().split()))

a2 = sorted(a)

ans = K//N
K %= N

number_list = [[0, 0] for _ in range(N)]

for i in range(N):
    pos = bisect.bisect(a2, a[i])

    number_list[i] = [i, pos]

for i in range(N):

    print(ans+1 if number_list[i][1] <= K else ans)
