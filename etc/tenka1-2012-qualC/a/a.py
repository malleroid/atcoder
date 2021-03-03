n = int(input())

ans = 0
for i in range(2, n):

    prime = True
    for j in range(2, i//2+1):

        if i % j == 0:
            prime = False
            break

    if prime is True:
        ans += 1

print(ans)
