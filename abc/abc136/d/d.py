S = input()

s = len(S)
ans = [0]*s
l_cnt = 0
r_cnt = 0
half = 0
for i in range(s-1):
    if S[i] == 'R':
        r_cnt += 1

    else:
        l_cnt += 1

    if S[i] == 'R' and S[i+1] == 'L':
        half = i

    if (S[i] == 'L' and S[i+1] == 'R') or i == s-2:

        if i == s-2:
            l_cnt += 1

        ans[half] = l_cnt//2+(r_cnt+1)//2
        ans[half+1] = (l_cnt+1)//2+r_cnt//2

        l_cnt = 0
        r_cnt = 0

print(*ans, sep=' ')
