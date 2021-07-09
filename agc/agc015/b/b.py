S = list(input())

n = len(S)
ans = 2*n-2
n -= 1
for i in range(1, n):

    ans += (n-i)+2*i if S[i] == 'U' else 2*(n-i)+i

print(ans)
