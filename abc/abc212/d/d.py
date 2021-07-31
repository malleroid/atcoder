import heapq

Q = int(input())
v = []
heapq.heapify(v)
add = 0
for i in range(Q):
    q = input()
    if q[0] == '1':
        s, t = map(int, q.split())
        heapq.heappush(v, t-add)

    elif q[0] == '2':
        s, t = map(int, q.split())
        add += t

    elif q[0] == '3':
        v_min = heapq.heappop(v)
        print(v_min+add)
