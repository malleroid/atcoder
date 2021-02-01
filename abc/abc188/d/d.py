N, C = map(int, input().split())

event = []

for i in range(N):

    a, b, c = map(int, input().split())

    event.append((a, c))
    event.append((b+1, -c))

event.sort()

ans = 0
fee = 0
prev = 0

for day, cha in event:

    ans += min(fee, C)*(day-prev)
    fee += cha
    prev = day

print(ans)
