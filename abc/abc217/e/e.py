import collections
import heapq

Q = int(input())
q = collections.deque()
hq = []
heapq.heapify(hq)

for i in range(Q):
    query = input()
    if query[0] == '1':
        n, x = map(int, query.split())
        q.append(x)

    elif query[0] == '2':
        if len(hq) == 0:
            print(q.popleft())
        else:
            print(heapq.heappop(hq))

    elif query[0] == '3':
        for v in q:
            heapq.heappush(hq, v)

        q.clear()
