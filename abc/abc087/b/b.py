A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0

for i in range(A+1):

    for j in range(B+1):

        num = X-500*i-100*j

        if num >= 0 and num // 50 <= C:
            ans += 1

print(ans)
