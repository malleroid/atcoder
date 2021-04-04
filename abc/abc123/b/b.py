T = [int(input()) for _ in range(5)]

mod = 10
num = 0
for i, time in enumerate(T):
    if time % 10 != 0 and time % 10 < mod:
        mod = time % 10
        num = i
t = T.pop(num)
ans = 0
for i in range(len(T)):
    ans += T[i]+10-T[i] % 10 if T[i] % 10 != 0 else T[i]

ans += t

print(ans)
