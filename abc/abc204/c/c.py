N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

p = [{i} for i in range(M)]

for i in range(M):

    p[AB[i][0]-1].add(AB[i][1])

ans = 0 if M != 0 else N

for i in range(M):

    q = list(p[i])
    q.sort()
    for j in range(len(q)):
        p[i] = p[i] | p[q[j]-1] | {i+1}

    print(p[i])
    ans += len(p[i])

print(ans)
