N = int(input())
S = input()

dp = [0]*N
cont_num = 0

for i in range(1, N):
    if S[i] == S[i-1]:
        cont_num += 1

    else:
        cont_num = 0

    dp[i] = dp[i-1]+i-cont_num

print(dp[-1])
