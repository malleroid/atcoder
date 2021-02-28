S = list(input())
N = int(input())

for i in range(N):

    l, r = map(int, input().split())

    s = S[l-1:r]
    rs = s[::-1]

    S[l-1:r] = rs

print(''.join(map(str, S)))
