import collections

N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)

rect = [0, 0]
for k, v in c.items():
    v = v//2
    if k > rect[0] and v >= 1:
        rect[1] = rect[0]
        rect[0] = k
        v -= 1

        if v >= 1:
            rect[1] = k

    elif k > rect[1] and v >= 1:
        rect[1] = k

ans = rect[0]*rect[1]
print(ans)
