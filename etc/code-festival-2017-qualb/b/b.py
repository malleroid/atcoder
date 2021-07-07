import collections

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

if M > N:
    print('NO')
    exit()

d = collections.Counter(D)
t = collections.Counter(T)

for k, v in t.items():

    if k not in d or d[k] < v:
        print('NO')
        exit()

print('YES')
