import itertools

X = int(input())

bin_X = bin(X)[2:][::-1]

active_list = [i for i, x in enumerate(bin_X) if x == '1']
len_active_list = len(active_list)

ans = []

for p in itertools.product([0, 1], repeat=len_active_list):
    tmp = 0
    for i, x in enumerate(p):
        if x == 1:
            tmp += 2**active_list[i]
    ans.append(tmp)

ans.sort()

print(*ans, sep='\n')
