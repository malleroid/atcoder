x = int(input())

ans = 0
ans += (x//11)*2

num = x % 11

if num == 0:
    pass

elif 0 < num <= 6:
    ans += 1

else:
    ans += 2

print(ans)
