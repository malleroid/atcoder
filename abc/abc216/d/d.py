import collections

N, M = map(int, input().split())

k = [0]*M
a = [0]*M
for _ in range(M):
    k[_] = int(input())
    a[_] = collections.deque(map(int, input().split()))

# print(k)
# print(a)
