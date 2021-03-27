N, M = map(int, input().split())
r = [0 for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())

    r[a-1] += 1
    r[b-1] += 1

print(*r, sep='\n')
