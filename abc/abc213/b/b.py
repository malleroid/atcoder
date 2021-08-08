N = int(input())
A = list(map(int, input().split()))

m1 = 0
m2 = 0
p1 = -1
p2 = -1
for i, v in enumerate(A):

    if A[i] > m1:
        m2 = m1
        p2 = p1
        m1 = A[i]
        p1 = i+1

    elif A[i] > m2:
        m2 = A[i]
        p2 = i+1

print(p2)
