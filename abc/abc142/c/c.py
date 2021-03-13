N = int(input())
A = list(map(int, input().split()))

ans = [0 for _ in range(N)]

for i, num in enumerate(A):
    ans[num-1] = i+1

print(*ans)
