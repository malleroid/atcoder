N = int(input())
X, Y = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0]*(Y+1) for _ in range(X+1)] for __ in range(N+1)]

print(dp)
