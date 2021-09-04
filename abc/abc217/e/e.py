import collections
import heapq

Q = int(input())
v = collections.deque()
flg = False
for i in range(Q):
    q = input()
    if q[0] == '1':
        n, x = map(int, q.split())
        if flg is False:
            v.append(x)
        else:
            heapq.heappush(w, x)

    elif q[0] == '2':
        if flg is False:
            print(v.pop())
        else:
            print(heapq.heappop(w))

    elif q[0] == '3':
        if flg is False:
            flg = True
            w = list(v)
            heapq.heapify(list(w))
