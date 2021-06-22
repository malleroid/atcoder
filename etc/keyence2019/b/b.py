S = list(input())
key = list('keyence')

for i in range(len(key)+1):
    left = key[:i]
    right = key[i:]

    s1 = S[:i]
    s2 = S[-(7-i):]

    if left == s1 and right == s2:
        print('YES')
        exit()

print('NO')
