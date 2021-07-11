N = int(input())
p = list(map(int, input().split()))

num = 0
now = 0
for i in range(N):
    if i+1 == p[i]:
        now += 1

        if now <= 1:
            num += 1

        else:
            now = 0

    else:
        now = 0

print(num)
