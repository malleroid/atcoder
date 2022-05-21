N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

d = {}

for i in range(N):
    d.setdefault(A[i], []).append(i+1)

sorted_d = sorted(d.items(), key=lambda x: x[0], reverse=True)


k, v = sorted_d[0]

for vv in v:
    if vv in B:
        print('Yes')
        exit()

print('No')
