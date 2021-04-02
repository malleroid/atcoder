N = int(input())
P = list(map(int, input().split()))

ans = 0
p_min = 2*10**5
for i in range(N):
    if P[i] <= p_min:
        ans += 1
        p_min = P[i]

print(ans)
