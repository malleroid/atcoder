A, B, C = map(int, input().split())

n = [A, B, C]
n.sort()

ans = 0
if A % 2 != 0 and B % 2 != 0 and C % 2 != 0:

    ans = n[0]*n[1]

print(ans)
