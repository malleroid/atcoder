import collections

N = int(input())
A = list(map(int, input().split()))

ans = 0

dict = collections.Counter(A)

for k, v in dict.items():

    N = N-v
    ans += v*N

print(ans)
