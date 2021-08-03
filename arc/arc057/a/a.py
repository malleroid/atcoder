A, K = map(int, input().split())

goal = 2*pow(10, 12)
now = A

if K == 0:
    print(goal-A)

else:
    ans = 0
    while now < goal:
        now += (1+K*now)
        ans += 1

    print(ans)
