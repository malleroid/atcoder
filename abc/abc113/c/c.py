N, M = map(int, input().split())
PY = [list(map(int, input().split()))+[i] for i in range(M)]

belong_prefecture = {}

for p, y, i in PY:
    belong_prefecture.setdefault(p, []).append([y, i])

recognized_number = []

for p in belong_prefecture:
    belong_prefecture[p].sort()

    for i in range(len(belong_prefecture[p])):
        y, n = belong_prefecture[p][i]
        recognized_number.append([n, "{:06}{:06}".format(p, i+1)])

recognized_number.sort()

for n, r in recognized_number:
    print(r)
