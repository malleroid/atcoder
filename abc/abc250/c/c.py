N, Q = map(int, input().split())

d = {i+1: i for i in range(N)}
n = [i+1 for i in range(N)]

for i in range(Q):
    x = int(input())
    if x == n[-1]:
        base_num_idx = len(n)-1
        swap_num_idx = len(n)-2

    else:
        base_num_idx = d[x]
        swap_num_idx = base_num_idx + 1

    swap_num = n[swap_num_idx]
    n[base_num_idx], n[swap_num_idx] = n[swap_num_idx], n[base_num_idx]

    d[x] = swap_num_idx
    d[swap_num] = base_num_idx

print(*n, sep=" ")
