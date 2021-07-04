P = int(input())
c = [0]*10

p = 1
for i in range(1, 11):
    p *= i
    c[i-1] = p

c.reverse()
ans = 0

for i in range(10):

    while c[i] <= P:
        P -= c[i]
        ans += 1

print(ans)
