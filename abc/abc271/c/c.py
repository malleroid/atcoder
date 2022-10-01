import collections

N = int(input())
a = list(map(int, input().split()))
a_unique = list(set(a))
duplicated_count = N-len(a_unique)
convert_target_numbers = [10**10] * duplicated_count

q_target_a = a_unique + convert_target_numbers
q_target_a.sort()
q = collections.deque(q_target_a)

ans = 0
while len(q) >= 1:
    if len(q) == 1:
        if q[0] == ans+1:
            ans += 1

        q.pop()
        break
    else:
        if q[0] == ans+1:
            ans += 1
            q.popleft()
        else:
            ans += 1
            p1 = q.pop()
            p2 = q.pop()

print(ans)
