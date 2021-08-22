import collections

Q = int(input())

q = collections.deque()
for i in range(Q):
    t, x = map(int, input().split())

    if t == 1:
        q.appendleft(x)

    elif t == 2:
        q.append(x)

    else:
        print(q[x-1])
