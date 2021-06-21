import collections

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

a = [0]*(N+1)
for i in range(N):
    a[A[i]] += 1

c = collections.Counter(C)

ans = 0
for k, v in c.items():
    ans += a[B[k-1]]*v

print(ans)
