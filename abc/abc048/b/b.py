a, b, x = map(int, input().split())

ans = 0
ceil = b//x
floor = (a-1)//x

ans = ceil-floor

print(ans)
