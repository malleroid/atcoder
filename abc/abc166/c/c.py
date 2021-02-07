N, M = map(int, input().split())
H = list(map(int, input().split()))

s = [1 for _ in range(N)]

for i in range(M):

    A, B = map(int, input().split())

    if H[A-1] == H[B-1]:
        s[A-1] = 0
        s[B-1] = 0

    else:
        k = A if H[A-1] < H[B-1] else B
        s[k-1] = 0

print(sum(s))
