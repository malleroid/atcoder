S = input()

ans = 10**5
num = 0
for i in range(len(S)):
    if i % 2 == 0 and int(S[i]) % 2 == 0:
        num += 1

    elif i % 2 == 1 and int(S[i]) % 2 == 1:
        num += 1

ans = min(ans, num)

num = 0
for i in range(len(S)):
    if i % 2 == 0 and int(S[i]) % 2 == 1:
        num += 1

    elif i % 2 == 1 and int(S[i]) % 2 == 0:
        num += 1

ans = min(ans, num)

print(ans)
