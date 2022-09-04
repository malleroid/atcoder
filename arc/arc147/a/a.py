import collections

N = int(input())
A = list(map(int, input().split()))
A.sort()

q = collections.deque(A)

ans = 0

while N > 1:
    max_q = q.pop()
    min_q = q[0]

    if max_q % min_q == 0:
        N -= 1

    else:
        q.appendleft(max_q % min_q)

    ans += 1

print(ans)
