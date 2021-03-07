N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(1, N):

    for j in range(i):

        num = (A[i]-A[j])**2
        ans += num


print(ans)
