import collections

N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    A[i] %= 200

c = collections.Counter(A)
ans = 0

for k, v in c.items():
    ans += v*(v-1)//2

print(ans)
