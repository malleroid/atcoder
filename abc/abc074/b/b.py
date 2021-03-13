N = int(input())
K = int(input())
x = list(map(int, input().split()))

ans = 0
for i in range(N):

    ans += 2*x[i] if K-x[i] >= x[i] else 2*(K-x[i])

print(ans)
