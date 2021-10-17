import collections

S = list(input())

n = len(S)

d = [S]
q = collections.deque(S)

for _ in range(n):
    p = q.popleft()
    q.append(p)
    d.append(list(q))

d.sort()

print(''.join(d[0]))
print(''.join(d[-1]))
