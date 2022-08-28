N = int(input())
s = [input() for _ in range(N)]

cnt_B_start_A_end = 0
cnt_B_start = 0
cnt_A_end = 0

for i in range(N):
    if s[i][0] == 'B' and s[i][-1] == 'A':
        cnt_B_start_A_end += 1
    elif s[i][0] == 'B':
        cnt_B_start += 1
    elif s[i][-1] == 'A':
        cnt_A_end += 1

ans = 0
for i in range(N):
    ans += s[i].count('AB')

ans += max(cnt_B_start_A_end-1, 0)

if cnt_B_start_A_end > 0 and cnt_B_start > 0:
    ans += 1
    cnt_B_start -= 1

if cnt_B_start_A_end > 0 and cnt_A_end > 0:
    ans += 1
    cnt_A_end -= 1

ans += min(cnt_B_start, cnt_A_end)

print(ans)
