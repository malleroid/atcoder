N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

ans = 0
for i in range(N):

    a1 = A1[:i+1]
    a2 = A2[i:]

    ans = max(ans, sum(a1)+sum(a2))

print(ans)
