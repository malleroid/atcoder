N = int(input())

ans = 0
d = len(str(N))

i = 4
while i <= d:
    if i <= d < i+3:
        ans += i//3*(N-10**(i-1)+1)

    else:
        ans += i//3*(10**(i+2)-10**(i-1))
    i += 3

print(ans)
