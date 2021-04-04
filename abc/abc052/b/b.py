N = int(input())
S = input()

x = 0
ans = 0
for i in range(N):
    if S[i] == 'I':
        x += 1
    elif S[i] == 'D':
        x -= 1

    ans = max(ans, x)

print(ans)
