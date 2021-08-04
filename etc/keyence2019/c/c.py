N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = sum(A)
b = sum(B)

if a < b:
    print(-1)

else:
    t = [0]*N
    for i in range(N):
        t[i] = A[i]-B[i]

    t.sort(reverse=True)

    now = 0
    p = 0
    ans = 0
    for i in range(N):
        if B[i] > A[i]:
            while B[i]-A[i] > now:
                now += t[p]
                p += 1
                ans += 1

            ans += 1
            now -= (B[i]-A[i])

    print(ans)
