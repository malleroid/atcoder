import collections

N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)

cnt = 0
for k, v in c.items():
    cnt += v*(v-1)//2

for i in range(N):
    print(cnt-c[A[i]]+1)
