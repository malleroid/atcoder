N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

A, B = [list(i) for i in zip(*AB)]

S = [A[i]/B[i] for i in range(N)]

s = sum(S)/2

i = 0
ans = 0
while s > 0:
    if S[i] > s:
        ans += B[i]*s
        s = 0
    else:
        ans += A[i]
        s -= S[i]
    i += 1

print(ans)
