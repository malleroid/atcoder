N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
current_b_sum = 0
for i in range(M):
    current_b_sum += A[i]
    ans += A[i]*(i+1)

current_b_num = ans

for i in range(N-M):
    current_b_num -= current_b_sum

    current_b_sum -= A[i]
    current_b_sum += A[i+M]
    current_b_num += A[i+M]*(M)

    ans = max(ans, current_b_num)

print(ans)
