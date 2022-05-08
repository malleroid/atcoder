H, W = map(int, input().split())
R, C = map(int, input().split())

ans = 0

if R >= 2:
    ans += 1

if R <= H-1:
    ans += 1

if C >= 2:
    ans += 1

if C <= W-1:
    ans += 1

print(ans)
