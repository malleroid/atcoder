N = int(input())
X = list(map(int, input().split()))
ans = 10**18
for i in range(1, 101):

    dist = 0

    for j in range(N):

        dist += (X[j]-i)**2

    ans = min(ans, dist)

print(ans)
