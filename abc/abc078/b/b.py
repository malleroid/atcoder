X, Y, Z = map(int, input().split())

ans = 1
X = X-Y-2*Z
print(ans+X//(Y+Z))
