N, M = map(int, input().split())

left = 0
right = 10**5
for i in range(M):
    L, R = map(int, input().split())

    left = max(left, L)
    right = min(right, R)

print(right-left+1 if right >= left else 0)
