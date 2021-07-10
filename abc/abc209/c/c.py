N = int(input())
C = list(map(int, input().split()))

p = pow(10, 9)+7

C.sort()
ans = 1
for i in range(N):
    num = C[i]-i if C[i]-i >= 0 else 0
    ans = ans*num % p

    if ans == 0:
        print(0)
        exit()

print(ans)
