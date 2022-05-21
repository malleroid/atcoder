N = int(input())
A = list(map(int, input().split()))

d = {}

for i in range(N):
    d.setdefault(A[i], []).append(i)

max_comb = N*(N-1)*(N-2)//6

ans = max_comb
for k, v in d.items():
    if len(v) >= 3:
        ans -= len(v)*(len(v)-1)*(len(v)-2)//6

    if len(v) >= 2:
        ans -= len(v)*(len(v)-1)//2*(N-len(v))

print(ans)
