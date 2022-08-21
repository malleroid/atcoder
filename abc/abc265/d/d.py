import bisect

N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

S = [0]*(N+1)

for i in range(N):
    S[i+1] = S[i]+A[i]

for i in range(N+1):
    x = i
    y = bisect.bisect_left(S, S[x]+P)

    if y > N or S[y]-S[x] != P:
        continue

    z = bisect.bisect_left(S, S[y]+Q)

    if z > N or S[z]-S[y] != Q:
        continue

    w = bisect.bisect_left(S, S[z]+R)

    if w > N or S[w]-S[z] != R:
        continue

    print('Yes')
    exit()

else:
    print('No')
