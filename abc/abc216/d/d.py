import collections

N, M = map(int, input().split())

a = [0]*M
cnt = [[] for _ in range(N)]
q = collections.deque()
for i in range(M):
    k = int(input())
    ai = list(map(int, input().split()))

    aq = collections.deque()
    for j in range(k):
        aq.append(ai[j]-1)

    a[i] = aq
    cnt[aq[0]].append(i)
    if len(cnt[aq[0]]) == 2:
        q.append(aq[0])

while q:
    n = q.pop()
    for i in range(2):
        index = cnt[n][i]
        a[index].popleft()
        if len(a[index]) != 0:
            num = a[index][0]
            cnt[num].append(index)
            if len(cnt[num]) == 2:
                q.append(num)

for i in range(len(a)):
    if len(a[i]) != 0:
        print('No')
        exit()

print('Yes')
