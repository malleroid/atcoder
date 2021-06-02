N, M = map(int, input().split())

ac = [0]*N
wa = [0]*N

for i in range(M):
    p, S = input().split()
    p = int(p)-1

    if S == 'AC':
        ac[p] = 1

    elif S == 'WA' and ac[p] == 0:
        wa[p] += 1

ac_cnt = sum(ac)
wa_cnt = sum([a*b for a, b in zip(ac, wa)])


print(ac_cnt, wa_cnt, sep=' ')
