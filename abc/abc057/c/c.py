import math
N = int(input())

s = math.sqrt(N)+1

ans = 10**10

for i in range(1, int(s)):
    if N % i == 0:
        j = N//i

        len_i = len(str(i))
        len_j = len(str(j))

        ans = min(ans, max(len_i, len_j))

print(ans)
