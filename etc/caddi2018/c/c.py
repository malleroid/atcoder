N, P = map(int, input().split())

if N >= 41:
    ans = 1

elif N == 1:
    ans = P

else:
    ans = 1
    i = 1
    while i**N <= P:

        if P % i**N == 0:
            ans = i

        i += 1

print(ans)
