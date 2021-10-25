import collections

N = int(input())
S = list(input())

q = collections.deque()
q.append('b')

n = 1
for i in range(1, 100):

    if n > N:
        print(-1)
        exit()

    elif n == N and S == list(q):
        print(i-1)
        exit()

    if i % 3 == 1:
        q.append('c')
        q.appendleft('a')

    elif i % 3 == 2:
        q.append('a')
        q.appendleft('c')

    elif i % 3 == 0:
        q.append('b')
        q.appendleft('b')

    n += 2
