import itertools

N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

set_T = set(T)

joined_s_len = len(''.join(S))
split_cnt = N-1
underscores = ['_'*(i+1) for i in range(16-split_cnt-joined_s_len+1)]

for p in itertools.permutations(S):
    for q in itertools.product(underscores, repeat=split_cnt):
        array_p = list(p)
        array_q = list(q)
        joined_q_len = len(''.join(array_q))
        if joined_s_len + joined_q_len > 16:
            continue

        if len(p) != 1:
            pq = list(itertools.chain.from_iterable(zip(array_p, array_q)))
            joined_p_q = ''.join(pq)+array_p[-1]
        else:
            joined_p_q = array_p[0]

        if len(joined_p_q) < 3:
            continue

        if joined_p_q not in set_T:
            print(joined_p_q)
            exit()

print("-1")
