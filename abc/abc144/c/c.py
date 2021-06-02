N = int(input())

i = 2
ans = N-1

while i**2 <= N:
    if N % i == 0:
        ans = min(ans, i+N//i-2)

    i += 1

print(ans)
