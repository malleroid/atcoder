N, A, B = map(int, input().split())

ans = 0
for i in range(1, N+1):

    s = list(map(int, str(i)))

    if A <= sum(s) <= B:
        ans += i

print(ans)
