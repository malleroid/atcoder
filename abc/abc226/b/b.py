N = int(input())
A = [list(input().split()) for _ in range(N)]

s = set()
for i in range(N):
    a = A[i][1:]
    element = ','.join(a)
    s.add(element)


print(len(s))
