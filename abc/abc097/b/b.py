X = int(input())

ans = 1
i = 2
while i**2 <= X:
    num = 2
    while i**num <= X:
        ans = max(ans, i**num)
        num += 1

    i += 1

print(ans)
