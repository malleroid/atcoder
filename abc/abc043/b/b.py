s = list(input())

ans = []
for i in range(len(s)):
    if s[i] == '0':
        ans.append('0')

    elif s[i] == '1':
        ans.append('1')

    elif s[i] == 'B' and len(ans) >= 1:
        ans.pop(-1)

print(''.join(ans))
