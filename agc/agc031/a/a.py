import collections

N = int(input())
S = input()

p = pow(10, 9)+7
c = collections.Counter(S)

ans = 1
for k, v in c.items():
    ans *= (v+1)
    ans %= p
print(ans-1)
