A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_min = min(a)
b_min = min(b)

ans = a_min+b_min

for i in range(M):

    x, y, c = map(int, input().split())

    n = a[x-1]+b[y-1]-c

    ans = min(ans, n)

print(ans)
