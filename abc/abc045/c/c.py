S = input()
n = len(S)

ans = 0
for i in range(2**(n-1)):

    bin_i = bin(i)[2:]
    code = ('0'*n+bin_i)[-n+1:]

    num = 0
    s = S
    for j in range(n-1):
        if code[j] == '1':
            left = s[:j+num+1]
            right = s[j+num+1:]

            s = left+'+'+right
            num += 1

    ans += eval(s)

print(ans)
